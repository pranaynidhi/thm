import string
import hashlib
word=""
l=open("md5_wordlist.txt","w")
z=open("wordlist.txt","w")
with open("cewl_wordlist.txt","r") as f:
    for word in f.read().splitlines():
        for i in range(99):
            for sp in string.punctuation:
                password=f'{word}{str(i).zfill(2)}{sp}'
                z.writelines(password)
                z.writelines("\n")
                l.writelines(hashlib.md5(f"{password}".encode("utf-8")).hexdigest())
                l.writelines("\n")
