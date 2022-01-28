from http.server import BaseHTTPRequestHandler, HTTPServer
from cryptography.fernet import Fernet
import requests
import rsa 
import FernetGetter
import urllib.parse
import pickle

"""This program create the second proxy
This proxy is the one exchanging data with the world wide web
The other proxy have to send the request to 127.0.0.1:8001
This program will take encrypted get request from the other proxy and decrypt it,
then make the public request and encrypt and send back the result
"""



class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """This function is the one called when the other proxy send an ecrypted get request
        The request is decrypted, sent into the web
        The response is encrypted and sent back to the first proxy"""

        # Get the encrypted request
        request_encrypted = self.path[3:].encode()
        print("I received the encrypted request : \n", str(request_encrypted))

        # Decrypt the request
        request_clear = fernet.decrypt(request_encrypted).decode()
        print("I decrypt the request : \n", str(request_clear))

        # Make the request and get the response
        response = requests.get(str(request_clear), headers=self.headers)
        response_clear = response.text
        print("I received the clear response : \n", response_clear)

        # Encrypt the response 
        response_encrypted = str(fernet.encrypt(response_clear.encode()))
        print("I encrypt the response : \n", response_encrypted)

        # Send the response code and the headers
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send back the encrypted response
        self.wfile.write(response_encrypted.encode("utf-8"))


# Get teh Fernet
fernet = FernetGetter.getKey()

# Launch the HTTP server on 127.0.0.1:8001
with HTTPServer(("127.0.0.1", 8001), handler) as server:
    server.serve_forever()