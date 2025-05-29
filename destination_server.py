from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class PQHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['Content-Length'])
        body = self.rfile.read(content_len).decode()
        print(f"[DEST] Received Encrypted PQ Payload:\n{body}")
    

        response={"status":"Processed","echo":body}
        self.send_response(200)
        self.send_header("Content-Type","application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def runserver():
    server = HTTPServer(('localhost',5000),PQHandler)
    print("[DEST] HTTP Server listening on port 5000")
    server.serve_forever()

if __name__ == "__main__":
    runserver()
