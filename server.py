from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import requests


def get_addr():
    """Get server addr."""
    if len(sys.argv) <= 2:
        return 8000
    else:
        return sys.argv[2]


class HTTPHandler(BaseHTTPRequestHandler):
    """Handle Request."""

    def do_GET(self):
        """Handle Get Method."""
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        """Handle POST Method."""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', len(post_data))
        self.end_headers()

        self.wfile.write(post_data)
        return


if __name__ == "__main__":
    print(get_addr())
    server_address = ('', get_addr())
    httpd = HTTPServer(server_address, HTTPHandler)
    httpd.serve_forever()
