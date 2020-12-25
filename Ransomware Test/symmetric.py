import base64
import hashlib

import test_key_gen

from Crypto import Random
from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key).digest()

    def _pad(self, s):
        block_size = 16
        remainder = len(s) % block_size
        padding_needed = block_size - remainder
        return s + bytes(padding_needed * ' ', 'utf-8')

    @staticmethod
    def _unpad(s):
        return s.rstrip()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc, decryption_key=None):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]

        if (decryption_key):
            self.key = hashlib.sha256(decryption_key).digest()

        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:]))


if __name__ == '__main__':
    key = test_key_gen.generate_key(bits=256, encode=True)
    cipher_obj = AESCipher(key)
    print(f'Key: {key}')
    with open('a.png', 'rb') as f:
        b_content = f.read()
    print(f'ORIG: {b_content}')
    enc = cipher_obj.encrypt(b_content)
    print(f'ENC: {enc}')
    dec = cipher_obj.decrypt(enc, decryption_key=key)
    print(f'DEC: {dec}')
    print(f'SAME: {b_content == dec}')


