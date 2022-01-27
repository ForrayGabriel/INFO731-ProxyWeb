from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

"""This program create the first proxy
This proxy is the one exchanging data with the web browser
The web browser proxy parameters have to be set on 127.0.0.1:8000
This program will take any get request and encrypt it, then send it to the other proxy on 127.0.0.1:8001
It will receive an encrypted response and decrypt it before sending it back to the web browser
"""

class handler(BaseHTTPRequestHandler):

    def do_CONNECT(self):
        """This function is the one called when the http server receive a CONNECT request
        I currently don't know how to handle this kinf of requests and just pass"""
        pass
        

    def do_GET(self):
        """This function is the one called when the http server receive a GET request 
        It take the requested url, encrypt it and send it to the other proxy, wait for
        a response, decrypt the response and send it back to the web browser"""

        #Get the clear request
        request_clear = self.path

        #Encrypt the request
        request_encrypted = request_clear
    
        #Generate the new url
        url = "http://127.0.0.1:8001/"+ request_encrypted

        # Ask the other proxy with the encrypted request and get the encrypted response
        response_encrypted = requests.get(url, headers=self.headers)
        
        #Decrypt the response
        response_clear = response_encrypted.text

        # Send the response code and the headers
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send the decrypted content
        self.wfile.write(response_clear.encode("utf-8"))
        self.wfile.close()

# Launch the HTTP server on 127.0.0.1:8000
with HTTPServer(("127.0.0.1", 8000), handler) as server:
    server.serve_forever()