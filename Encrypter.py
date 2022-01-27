from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

class handler(BaseHTTPRequestHandler):

    def printMessage(self, message):
        print(message)

    def do_CONNECT(self):

        url = self.path

        #resp = requests.get(url, headers=self.headers)
        #print("ceci est la réponse " + resp.text)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World!"
        self.wfile.write(message.encode("utf-8"))

    def do_GET(self):
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        self.printMessage("Je recois une demande :")
        """print(self.path)
        print(self.command)
        print(self.headers)"""

        url = "http://127.0.0.1:8001/"+self.path

        print(url)
        # Ask the other proxy
        resp = requests.get(url, headers=self.headers)
        print("ceci est la réponse " + resp.text)

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        self.wfile.write(resp.text.encode("utf-8"))
        self.wfile.close()

with HTTPServer(("127.0.0.1", 8000), handler) as server:
    server.serve_forever()