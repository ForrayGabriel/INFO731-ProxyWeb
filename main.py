import Decrypter
import Encrypter
import rsa # pip install rsa

encrypter = Encrypter.handler() # serveur qui chiffre la requête de user vers decrypter
decrypter = Decrypter.handler() # serveur qui chiffre la réponse web vers encrypter

# création des clés 
pubkey1, privkey1 = rsa.newkeys(512)
pubkey2, privkey2 = rsa.newkeys(512)


'''
user --(req en clair)--> encrypter (proxy1) --(req chiffrée avec pubkey1)--> decrypter (proxy2) --(req déchiffrée avec privkey1)--> web

web --(req en clair)--> decrypter (proxy2) --(req chiffrée avec pubkey2)--> encrypter (proxy1) --(req déchiffrée avec privkey2)--> user
'''
# on envoie la requête à notre encrypter

# on recoit le resultat par notre decrypter
