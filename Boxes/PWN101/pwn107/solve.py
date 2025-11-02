#!/usr/bin/env python3
from pwn import *
import dotenv, os

dotenv.load_dotenv("../.env")
RHOST, RPORT = str(os.environ["RHOST"]), 9003

exe = ELF("./")

context.binary = exe
context.log_level = "debug"



def conn():
    r = process([exe.path])
    # r = remote(RHOST, RPORT)

    return r


def main():
    io = conn()

    io.sendlineafter(b'<++>', b'<++>')

    io.interactive()


if __name__ == "__main__":
    main()
