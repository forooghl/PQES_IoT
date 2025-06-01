import socket, time, random, threading, json

def simulate_device(device_id):
    host = "localhost"
    port = 8081
    while True:
        try:
            heart_rate = random.randint(60,100)
            temp = round(random.uniform(36.0, 38.5), 1)
            data = f"Device:{device_id}, HR:{heart_rate}, Temp:{temp}"

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,port))
            sock.send(data.encode())
            response = sock.recv(2048).decode()
            sock.close()
            
            print(f"[IOT-{device_id}] status: {response}")
        except Exception as e:
            print(f"[IOT-{device_id}] Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=simulate_device, args=(f"IoT-{i}",)).start()