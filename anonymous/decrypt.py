#!/usr/bin/env python3

cipher = input("Enter two character: ")
print(cipher)
first= cipher[0]
second = cipher[1]
ans = (ord(first)+(ord(second)%65)+1)
print(ans)
print(chr(ans))
