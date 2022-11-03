#!/usr/bin/env python3

import sys, os, socket
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST_NAME = socket.gethostbyname(socket.gethostname())
PORT = 8220

print(HOST_NAME)

def read_file(path):
    try:
        with open(path) as f:
            file = f.read()
    except Exception as e:
        file = e
    return file


def serve_html(self):
	file = read_file(self.path)
	self.send_response(200, "OK")
	self.end_headers()
	self.wfile.write(bytes(file, "utf-8"))

def serve_error(self):
	self.send_response(403)
	self.end_headers()

def serve_now_spotify(self):
    os.system('notify-read -n1 -a "spotify" > ' + os.path.expanduser('~') + '/.cache/notifications_spotify.log')
    file = read_file(os.path.expanduser('~') + "/.cache/notifications_spotify.log")
    self.send_response(200, "OK")
    self.send_header("Content-type", 'text/plain')
    self.end_headers()
    self.wfile.write(bytes(file, "utf-8"))



class PythonServer(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/index':
            self.path = './web/index.html'
            serve_html(self)
        if self.path == '/now/spotify':
            serve_now_spotify(self)
        else:
            #print("superted")
            super().do_GET()


	
if __name__ == "__main__":
    server = HTTPServer((HOST_NAME, PORT), PythonServer)
    print(f"Server started http://{HOST_NAME}:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("Server stopped successfully")
        sys.exit(0)