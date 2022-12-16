import bcrypt
import base64

salt   = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.'
mypass = b'$2b$12$LJ3m4rzPGmuN1U/h0IO55.3h9WhI/A0Rcbchmvk10KWRMWe4me81e'

with open('word.txt') as fp:
    line = fp.readline()
    while line:
        #bpass = line.strip().encode('ascii')
        #[UPDATED]
        bpass = line.strip().encode('ascii','ignore')
        passed= str(base64.b64encode(bpass))
        hashAndSalt = bcrypt.hashpw(passed.encode(), salt)
        print("Password {}".format(line.strip()))
        
        if ( hashAndSalt == mypass ):
            print(hashAndSalt)
            print("Password {}".format(line.strip()))
            print("============================FOUND========================")
            break
        line = fp.readline()
