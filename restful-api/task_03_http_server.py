#!/usr/bin/python3
import http.server
import json
"""
This module implements a simple HTTP server that responds to GET requests
 on two endpoints: /data and /status.
 The server listens on localhost at port 8000.
-The /data endpoint returns a JSON object containing sample data.
-The /status endpoint returns a plain text response with the message "OK".
-For any other endpoint, the server responds with a 404 Not Found error.
"""


PORT = 8000
HOST = "localhost"


class HTTPserver(http.server.BaseHTTPRequestHandler):
    """This class handles HTTP GET requests and responds with appropriate data
      based on the requested endpoint."""
    def do_GET(self):
        """Define the behavior for GET requests. It checks the requested path
          and responds with JSON data for /data, a plain text message
            for /status, and a 404 error for any other path."""
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")


if __name__ == "__main__":
    server = http.server.HTTPServer((HOST, PORT), HTTPserver)
    server.serve_forever()
