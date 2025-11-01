# Chill Hack

[https://tryhackme.com/r/room/chillhack](https://tryhackme.com/r/room/chillhack)

#  Task 1 - Investigate!

Chill the Hack out of the Machine.
Easy level CTF.  Capture the flags and have fun!

## Answer the questions below
*User Flag*
`{USER-FLAG: e8vpd3323cfvlp0qpxxx9qtr5iq37oww}`
*Root Flag*
`<++>`


# Notes
/usr/bin/gettext.sh

# Timeline
1. Ferox found /secret where I can inject *some* commands
2. I can inject commands by bypassing whitelist with a `\` in the middle of a word
3. Exploit and get shell
4. Can run a script as another user, inject a `/bin/bash` and get shell.
5. Ran linpeas, found mysql db hosted locally and some files in `/var/www/files`

# Ideas
 - Chisel or ssh-portforward to access the db, maybe run sqlmap?
 - Investigate the alternative webroot
