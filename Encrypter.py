from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.fernet import Fernet
import requests
import rsa
import FernetGetter

"""This program create the first proxy
This proxy is the one exchanging data with the web browser
The web browser proxy parameters have to be set on 127.0.0.1:8000
This program will take any get request and encrypt it, then send it to the other proxy on 127.0.0.1:8001
It will receive an encrypted response and decrypt it before sending it back to the web browser
"""

class handler(BaseHTTPRequestHandler):

    def do_CONNECT(self):
        pass

    def do_GET(self):
        """This function is the one called when the http server receive a GET request 
        It take the requested url, encrypt it and send it to the other proxy, wait for
        a response, decrypt the response and send it back to the web browser"""

        #Get the clear request
        request_clear = self.path
        print("I receive the clear request : \n", request_clear)

        #Encrypt the request
        request_encrypted = str(fernet.encrypt(request_clear.encode()))
        print("I encrypted the request as : \n", request_encrypted)

        #Generate the new url
        url = "http://127.0.0.1:8001/"+ request_encrypted

        # Ask the other proxy with the encrypted request and get the encrypted response
        response = requests.get(url, headers=self.headers)
        response_encrypted = response.text[2:].encode()
        print("I received the crypted response : \n", response.text)

        #Decrypt the response
        response_clear = fernet.decrypt(response_encrypted).decode()
        print("I decrypted the response : \n", response_clear)

        # Send the response code and the headers
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send the decrypted content
        self.wfile.write(response_clear.encode("utf-8"))


# Get the keys
fernet = FernetGetter.getKey()

# Launch the HTTP server on 127.0.0.1:8000
with HTTPServer(("127.0.0.1", 8000), handler) as server:
    server.serve_forever()