#!/usr/bin/python3
"""This module implements a simple HTTP server that responds to GET requests
 on two endpoints: /data and /status."""

import http.server
import socketserver
import json


class HTTPserver(http.server.BaseHTTPRequestHandler):
    """This class handles HTTP GET requests and responds with appropriate data
      based on the requested endpoint."""
    def do_GET(self):
        """Define the behavior for GET requests. It checks the requested path
          and responds with JSON data for /data, a plain text message
            for /status, and a 404 error for any other path."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf8"))

        elif self.path == "/info":
            info = {"version": "1.0", "description":
                    "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


PORT = 8000
with socketserver.TCPServer(("", PORT), HTTPserver) as httpd:
    httpd.serve_forever()
