from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class PQHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        body = self.rfile.read(content_len).decode()
        
        body_json = json.loads(body)
        print(f"[DEST] Received Encrypted PQ Payload:\ncert: {body_json["cert"]}\ncipherText: {body_json["ciphertext"][0:13]}...")
    

        response={"status":"Processed","echo":body}
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def runserver():
    server = HTTPServer(('localhost',5050),PQHandler)
    print("[DEST] HTTP Server listening on port 5050")
    server.serve_forever()

if __name__ == "__main__":
    runserver()
