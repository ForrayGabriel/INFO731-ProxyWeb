from http.server import BaseHTTPRequestHandler, HTTPServer
import requests

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
        request_encrypted = self.path[1:]

        # Decrypt the request
        request_clear = request_encrypted

        # Make the request and get the response
        response_clear = requests.get(request_clear, headers=self.headers)

        # Encrypt the response 
        response_encrypted = response_clear.text

        # Send the response code and the headers
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send back the encrypted response
        self.wfile.write(response_encrypted.encode("utf-8"))
        self.wfile.close()

# Launch the HTTP server on 127.0.0.1:8001
with HTTPServer(("127.0.0.1", 8001), handler) as server:
    server.serve_forever()