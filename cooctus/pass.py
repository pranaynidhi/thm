#!/usr/bin/python3

def encode(pwd):
    enc = ''
    for i in pwd:
        if ord(i) > 110:
            num = (13 - (122 - ord(i))) + 96
            enc += chr(num)
        else:
            enc += chr(ord(i) + 13)
    return enc

s = 'abcdefghijklmnopqrstuvwxyz'
clear = list(s)
encoded = list(encode(s))

pwd = "pureelpbxr"
dec = ""

for i in pwd:
    dec += clear[encoded.index(i)]

print(dec)
