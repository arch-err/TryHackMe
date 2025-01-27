# Corridor

Can you escape the Corridor?

[https://tryhackme.com/r/room/corridor](https://tryhackme.com/r/room/corridor)

---

# Task 1 - Escape the Corridor

You have found yourself in a strange corridor. Can you find your way back to where you came?

In this challenge, you will explore potential IDOR vulnerabilities. Examine the URL endpoints you access as you navigate the website and note the hexadecimal values you find (they look an awful lot like a hash, don't they?). This could help you uncover website locations you were not expected to access.

## Answer the questions below
*What is the flag?*
`flag{2477ef02448ad9156661ac40a6b8862e}`

---

# Timeline
1. Webpage is a image of a corridor with clickable doors. Door hrefs looks like hashes of some kind.
2. The hashes are md5 of numbers from 1-13
3. I generate md5 of dorr #14 -> url not found
4. md5 of dorr #0 -> flag
