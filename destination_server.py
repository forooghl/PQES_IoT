from http.server import BaseHTTPRequestHandler, HTTPServer
from oqs import KeyEncapsulation
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import json

kem = KeyEncapsulation("Kyber512")
kem_public_key = kem.generate_keypair()
with open("kyber_public_key.bin", "wb") as f:
    f.write(kem_public_key)

print("[DEST] Public key saved to kyber_public_key.bin")

class PQHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        body = self.rfile.read(content_len).decode()
        payload = json.loads(body)
        
        try:
            cert = payload["cert"]
            ciphertext = bytes.fromhex(payload["ciphertext"])
            nonce = bytes.fromhex(payload["nonce"])
            encrypted_data = bytes.fromhex(payload["data_enc"])

            # Decrypt the shared secret
            shared_secret = kem.decap_secret(ciphertext)
            aes_key = shared_secret[:32]
            aesgcm = AESGCM(aes_key)

            decrypted = aesgcm.decrypt(nonce, encrypted_data, None).decode()
            
            print(f"[DEST] Received Encrypted PQ Payload:\ncert: {cert}\ncipherText: {encrypted_data}...")

            response={"status":"Processed","echo":body}
            self.send_response(200)
            self.send_header("Content-Type","application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(f"ERROR: {e}".encode())

def runserver():
    server = HTTPServer(('localhost',5050),PQHandler)
    print("[DEST] HTTP Server listening on port 5050")
    server.serve_forever()

if __name__ == "__main__":
    runserver()
