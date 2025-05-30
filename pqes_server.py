import socket, threading, requests, json
from oqs import Signature, KeyEncapsulation
import psutil, time, select, os

translation_table={}

def generate_pq_certificate(ip):
    kem = KeyEncapsulation("Kyber512")
    kem_pk = kem.generate_keypair()

    sig = Signature("Dilithium2")
    sig_pk = sig.generate_keypair()
    cert = f"PQ-CERT-{ip[:5]}-{sig_pk[:8].hex()}"
    return cert, sig_pk, kem_pk, sig

def handle_client(conn, addr):
    ip = addr[0]
    if ip not in translation_table:
        cert, sig_pk, kem_pk, sig = generate_pq_certificate(ip)
        translation_table[ip] = (cert, sig_pk, kem_pk, sig)
        print(f"[PQES] Generated PQ Cert for {ip}: {cert}")
    else:
        cert, sig_pk, kem_pk, sig = translation_table[ip]

    data = conn.recv(2048).decode()
    print(f"[PQES] Received from {ip}: {data}")

    start_time = time.perf_counter()

    kem = KeyEncapsulation("Kyber512")
    ciphertext, shared_secret = kem.encap_secret(kem_pk)

    signature = sig.sign(data.encode())

    payload = {
        "cert": cert,
        "ciphertext": ciphertext.hex(),
        "data": data,
        "signature": signature.hex()   
        }

    try:
        response = requests.post("http://localhost:5050", json=payload)
        reply = response.json()
        conn.send(json.dumps(reply).encode())
    except Exception as e:
        conn.send(f"ERROR: {e}".encode())
    conn.close()

    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1000
    print(f"[PQES] ↔ Latency: {elapsed:.2f} ms | Payload: {len(json.dumps(payload))} bytes")

def runPQES():
    host = 'localhost'
    port = 8081
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(5)
    print("[PQES] Listening on port 8081")

    while True:
        readable, _, _ = select.select([server_socket], [], [], 1)
        if readable:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == "__main__":
    runPQES()