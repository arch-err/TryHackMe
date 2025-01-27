# Different CTF

interesting room, you can shoot the sun

[https://tryhackme.com/r/room/adana](https://tryhackme.com/r/room/adana)

---

# Task 1 - Basic scan

10.10.34.237

*Hello there
We will tend to think differently in this room.
In fact, we will understand that what we see is not what we think, and if you go beyond the purpose, you will disappear in the room, fall into a rabbit hole.*

## Answer the questions below

*How many ports are open ?*
`2`
*What is the name of the secret directory ?*
`Announcements`

---

# Task 2 - Localhost

This place will be solved from inside after receiving a shell

## Answer the questions below
*Web flag ?*
`THM{343a7e2064a1d992c01ee201c346edff}`
*User flag ?*
`THM{8ba9d7715fe726332b7fc9bd00e67127}`
*Root flag ?*
`THM{c5a9d3e4147a13cbd1ca24b014466a6c}`


# Notes
/etc/ImageMagick-6/mime.xml

# Timeline
1. Enum found ftp and http, http is a wp-site
2. ferox found /announcements/wordlist.txt
3. Also found a jpeg in announcements, cracked it with wordlist and extracted ftp creds
4. dump ftp using a cool wget command, found wp-config.php
5. Found out that phpMyAdmin is a thing, logged in with creds from wp-config.php
6. Found subdomain.blabla.thm, this is the ftp site
7. php shell -> boom revshell!!
