def get_keys():
    with open("keys.txt") as f:
        return f.readline()[:-1].split(",")

def get_encrypter_key():
    return get_keys()[0]

def get_decrypter_key():
    return get_keys()[1]