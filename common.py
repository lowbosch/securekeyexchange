import binascii
import sys

def crypt(text, offset):
    key = getkey(offset, len(text))
    cipher = [a^b for (a,b) in zip(text, key)]
    return bytes(cipher)

def getkey(offset, length):
    with open('keymaterial', "rb") as f:
        f.seek(offset)
        key = f.read(length)
        return key
