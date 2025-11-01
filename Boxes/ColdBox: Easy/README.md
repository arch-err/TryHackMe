# ColddBox: Easy
An easy level machine with multiple ways to escalate privileges.

[https://tryhackme.com/room/colddboxeasy](https://tryhackme.com/room/colddboxeasy)

# Task 1 - boot2Root

Can you get access and get both flags?

Good Luck!.


Doubts and / or help in twitter: @martinfriasc or @ColddSecurity

Thumbnail box image credits, designed by Freepik from www.flaticon.es


## Answer the questions below
*user.txt*
`RmVsaWNpZGFkZXMsIHByaW1lciBuaXZlbCBjb25zZWd1aWRvIQ==`
*root.txt*
`wqFGZWxpY2lkYWRlcywgbcOhcXVpbmEgY29tcGxldGFkYSE=`

# Timeline
1. Enumerate, find wp
2. wpscan, enum users
3. wpscan, brute passwords
4. log in wordpress
5. Edit theme, get shell
6. find a password in wp-config.php
7. su to user C0ldd
8. get user.txt
9. sudo -l gives ftp... really?
10. sudo ftp -> ROOT
