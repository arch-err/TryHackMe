# RootMe

A ctf for beginners, can you root me?

(https://tryhackme.com/r/room/rrootme)[https://tryhackme.com/r/room/rrootme]

---

# Task 1 - Deploy the machine
Connect to TryHackMe network and deploy the machine. If you don't know how to do this, complete the OpenVPN room first.

## Answer the questions below

*Deploy the machine*

---

# Task 2 - Reconnaissance

First, let's get information about the target.

## Answer the questions below

*Scan the machine, how many ports are open?*
`2`
*What version of Apache is running?*
`2.4.29`
*What service is running on port 22?*
`ssh`
*Find directories on the web server using the GoBuster tool.*
`No ans needed`
*What is the hidden directory?*
`/panel/`

---

# Task 3 - Getting a shell

Find a form to upload and get a reverse shell, and find the flag.

## Answer the questions below
*user.txt*
`<++>`

---

# Task 4 - Privilege escalation

Now that we have a shell, let's escalate our privileges to root.

## Answer the questions below

*Search for files with SUID permission, which file is weird?*
`/usr/bin/python`
*Find a form to escalate your privileges.*
`/usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'`
*root.txt*
`THM{pr1v1l3g3_3sc4l4t10n}`
