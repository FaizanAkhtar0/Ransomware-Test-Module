import os
import base64

def generate_key(bits, encode=False):
    content = os.urandom(bits)

    if (encode):
        return base64.b64encode(content)

    return content


if __name__ == "__main__":
    print(generate_key(32))