# HA Joker CTF

Batman hits Joker.

[https://tryhackme.com/r/room/jokerctf](https://tryhackme.com/r/room/jokerctf)

---

# Task 1 - HA Joker CTF

We have developed this lab for the purpose of online penetration practices. Solving this lab is not that tough if you have proper basic knowledge of Penetration testing. Let’s start and learn how to breach it.

1. Enumerate Services
 - Nmap
2. Bruteforce
 - Performing Bruteforce on files over http
 - Performing Bruteforce on Basic Authentication
3. Hash Crack
 - Performing Bruteforce on hash to crack zip file
 - Performing Bruteforce on hash to crack mysql user
4. Exploitation
 - Getting a reverse connection
 - Spawning a TTY Shell
5. Privilege Escalation
 - Get root taking advantage of flaws in LXD

## Answer the questions below

*Enumerate services on target machine.*
`Done`
*What version of Apache is it?*
`2.4.29`
*What port on this machine not need to be authenticated by user and password?*
`80`
*There is a file on this port that seems to be secret, what is it?*
`secret.txt`
*There is another file which reveals information of the backend, what is it?*
`phpinfo.php`
*When reading the secret file, We find with a conversation that seems contains at least two users and some keywords that can be intersting, what user do you think it is?*
`joker`
*What port on this machine need to be authenticated by Basic Authentication Mechanism?*
`8080`
*At this point we have one user and a url that needs to be aunthenticated, brute force it to get the password, what is that password?*
`hannah`
*Yeah!! We got the user and password and we see a cms based blog. Now check for directories and files in this port. What directory looks like as admin directory?*
`<++>`
*We need access to the administration of the site in order to get a shell, there is a backup file, What is this file?*
`<++>`
*We have the backup file and now we should look for some information, for example database, configuration files, etc ... But the backup file seems to be encrypted. What is the password?*
`<++>`
*Remember that... We need access to the administration of the site... Blah blah blah. In our new discovery we see some files that have compromising information, maybe db? ok what if we do a restoration of the database! Some tables must have something like user_table! What is the super duper user?*
`admin`
*Super Duper User! What is the password?*
`<++>`
*At this point, you should be upload a reverse-shell in order to gain shell access. What is the owner of this session?*
`<++>`
*This user belongs to a group that differs on your own group, What is this group?*
`<++>`
*Spawn a tty shell.*
`<++>`
*In this question you should be do a basic research on how linux containers (LXD) work, it has a small online tutorial. Googling "lxd try it online".*
`<++>`
*Research how to escalate privileges using LXD permissions and check to see if there are any images available on the box.*
`<++>`
*The idea here is to mount the root of the OS file system on the container, this should give us access to the root directory. Create the container with the privilege true and mount the root file system on /mnt in order to gain access to /root directory on host machine.*
`<++>`
*What is the name of the file in the /root directory?*
`<++>`


# Notes
<++>

# Timeline
<++>
