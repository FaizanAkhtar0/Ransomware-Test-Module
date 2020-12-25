import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

class RSACipher:

    def __init__(self):
        self.bit_len = 2048
        self.private_key_PEM = None
        self.public_key_PEM = None
        self.key = None

    def generate_keys(self):
        self.key = RSA.generate(self.bit_len)
        self.private_key_PEM = self.key.export_key('OpenSSH')
        self.public_key_PEM = self.key.publickey().export_key('OpenSSH')

    def encrypt(self, data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.encrypt(data)

    def decrypt(self, data):
        cipher = PKCS1_OAEP.new(self.key)
        return cipher.decrypt(data)

    def save_to_files(self, path):
        private_key_path = os.path.join(path, 'private.key')
        public_key_path = os.path.join(path, 'public.key')

        with open(private_key_path, 'wb') as f:
            f.write(self.key.export_key())

        with open(public_key_path, 'wb') as f:
            f.write(self.key.publickey().export_key())

if __name__ == "__main__":
    cipher = RSACipher()
    cipher.generate_keys()
    try:
        os.makedirs('Hacker_keys')
    except:
        pass
    path = os.getcwd() + '\\Hacker_keys'
    cipher.save_to_files(path)
    # enc = cipher.encrypt(b'HELLO! NIGGA')
    # print(f"ENC: {enc}")
    # dec = cipher.decrypt(enc)
    # print(f"DEC: {dec}")
    # print(cipher.private_key_PEM)
    # print(cipher.public_key_PEM)