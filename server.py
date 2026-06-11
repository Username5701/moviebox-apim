from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/commands':
            # Run moviebox --help and return output
            try:
                result = subprocess.run(['moviebox', '--help'], capture_output=True, text=True, timeout=10)
                output = result.stdout + result.stderr
                self.send_response(200)
                self.end_headers()
                self.wfile.write(output.encode())
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'MovieBox API Runner - Use /commands to see available commands')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    print(f"Starting server on port {port}")
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()