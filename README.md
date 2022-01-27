# INFO731 - ProxyWeb
### Forray Gabriel - Gobji Zied - Koeberle Célien 
  

*The goal of this project is two create a doble proxy system between which the communication are encrypted.*

### **How tu use**

1. Clone the repository in a local folder
2. You can edit the security keys in the keys.txt file
3. Launch Encrypter.py and Decrypter.py in two cmds
4. In your web browser, set your proxy setting to the adresse 127.0.0.1 and the port 8000

### **How it works**

When launched, both programs go get the keys from de keys.txt file. Then the Encrypter.py file launch the first proxy, and the Decrypter.py file launch the second one.  

The first proxy is the one that receive the requests from the web browser. When it gets one "GET" request, it encrypt it and send it to the second proxy.  
The second proxy get the request, decrypt it and use it to get a result from the web. It then encrypt the response and send it back to the first proxy.  
The first proxy now just decrypt the response and send it to the web browser.  

Both encryption and decryption are made using XXXXXXXXXX


### **Problems**
Making web requests was way more difficult than we though. For now, this system can only work on certain websites that does not need a CONNECT request first that we don't know how to handle yet.  
For now the system only works with http requests and can only transfer html without the corresponding css.  
Most website will not work. As an exemple where the text is correctly transfered, you can try to go on http://forrayg.xyz/mass_shooting_us
