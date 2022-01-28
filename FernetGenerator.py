from cryptography.fernet import Fernet
import pickle

key = Fernet.generate_key()
fernet = Fernet(key)

with open('key.key', 'wb') as f:
  pickle.dump(fernet, f)

