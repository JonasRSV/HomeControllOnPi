from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import requests
import alexa
import json


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

        response = alexa.lambda_handler(json.loads(post_data))
        json_data = json.dumps(response)

        byte_data = json_data.encode()

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-Length', len(byte_data))
        self.end_headers()

        self.wfile.write(byte_data)
        return


if __name__ == "__main__":
    print(get_addr())
    server_address = ('', get_addr())
    httpd = HTTPServer(server_address, HTTPHandler)
    httpd.serve_forever()
