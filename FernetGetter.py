import rsa
import pickle

def getKey():
    with open('key.key', 'rb') as file:
        key = pickle.load(file)
    return key