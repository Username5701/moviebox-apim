from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import subprocess
from urllib.parse import parse_qs, urlparse

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/run':
            query = parse_qs(parsed.query)
            cmd = query.get('cmd', [''])[0]
            
            if cmd == 'movie-help':
                result = subprocess.run(['moviebox', '--help'], capture_output=True, text=True)
            elif cmd == 'trending':
                result = subprocess.run(['moviebox', 'v2', 'homepage-content'], capture_output=True, text=True)
            else:
                result = "Available commands: movie-help, trending"
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str(result).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Use /run?cmd=movie-help')

port = int(os.environ.get('PORT', 10000))
HTTPServer(('0.0.0.0', port), Handler).serve_forever()