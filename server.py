from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import subprocess

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'MovieBox API Runner - Use Render Shell to run commands')
        elif self.path == '/commands':
            # Run moviebox --help and return output
            result = subprocess.run(['moviebox', '--help'], capture_output=True, text=True)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(result.stdout.encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()