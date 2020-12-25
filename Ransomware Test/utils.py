import os
import random

ASCII_LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
ASCII_UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DIGITS = '0123456789'


def shred(file_name,  passes=25):
    def generate_data(length):
        chars = ASCII_LOWERCASE + ASCII_UPPERCASE + DIGITS
        return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

    if not os.path.isfile(file_name):
        return False

    ld = os.path.getsize(file_name)
    with open(file_name,  "w") as fh:
        for _ in range(int(passes)):
            data = generate_data(ld)
            fh.write(data)
            fh.seek(0,  0)
    os.remove(file_name)

