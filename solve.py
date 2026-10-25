from pwn import *

HOST = "0.cloud.chals.io"
PORT = 30804

io = remote(HOST, PORT)

# Receive the welcome banner and name prompt
print(io.recvuntil(b"Enter your name:").decode())

# Send a name
io.sendline(b"player")

# Display the server's response
print(io.recvrepeat(2).decode(errors="replace"))

io.interactive()
