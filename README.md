# INFO731 - ProxyWeb
### Forray Gabriel - Gobji Zied - Koeberle Célien 
  

*The goal of this project is two create a doble proxy system between which the communication are encrypted.*

### **How tu use**

1. Clone the repository in a local folder
2. You can regenarte the Fornet by launching FernetGenarator.py
3. Launch Encrypter.py and Decrypter.py in two cmds
4. In your web browser, set your proxy setting to the adresse 127.0.0.1 and the port 8000

### **How it works**

The FernetGenarator create a Fernet object from the cryptography librairy and stocks it in the key.key file.  

When launched, both programs go get the Fornet from the key.key file using FernetGetter.py. Then the Encrypter.py file launch the first proxy, and the Decrypter.py file launch the second one.  

The first proxy is the one that receive the requests from the web browser. When it gets one "GET" request, it encrypt it using the Fornet and send it to the second proxy.  

The second proxy get the request encrypted, decrypt it with the Fornet and use it to get a result from the web. It then encrypt the response and send it back to the first proxy.  

The first proxy now just decrypt the response and send it to the web browser.  

### **Problems**
Making web requests was way more difficult than we though. For now, this system can only work on certain websites that does not need a CONNECT request first that we don't know how to handle yet, so none of the https websites.  

Sometime the css dones't want to pass but sometime it works.  

Most website will not work. As an exemple where the text is correctly transfered, you can try to go on http://www.http2demo.io/ that works pretty well.
