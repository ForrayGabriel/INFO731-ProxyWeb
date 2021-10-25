from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

    def do_CONNECT(self):
        print(self.path)
        print(self.command)
        print(self.headers)

        url = "https://" + self.path

        resp = requests.get(url, headers=self.headers)
        print("ceci est la réponse " + resp.text)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(bytes(resp.text,'utf-8'))



with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()