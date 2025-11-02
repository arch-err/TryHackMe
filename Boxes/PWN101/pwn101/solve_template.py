#!/usr/bin/env python3
from pwn import *
import dotenv, os

dotenv.load_dotenv("../.env")
RHOST, RPORT = str(os.environ[""]), 9001

exe = ELF("./pwn101-1644307211706.pwn101_patched")

context.binary = exe
context.log_level = "debug"



def conn():
    r = process([exe.path])
    # r = remote("addr", 1337)

    return r


def main():
    r = conn()

    r.interactive()


if __name__ == "__main__":
    main()
