from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"STATUS: OK")
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"🚀 Production Web App running smoothly!")

server = HTTPServer(('0.0.0.0', 8080), HealthHandler)
print("🚀 Health-aware server starting on port 8080...")
server.serve_forever()
