# Easy Peasy
Practice using tools such as Nmap and GoBuster to locate a hidden directory to get initial access to a vulnerable machine. Then escalate your privileges through a vulnerable cronjob.

[https://tryhackme.com/room/easypeasyctf](https://tryhackme.com/room/easypeasyctf)

---

# Task 1 - Enumeration through Nmap

Deploy the machine attached to this task and use nmap to enumerate it.

## Answer the questions below
*How many ports are open?*
`3`
*What is the version of nginx?*
`1.16.1`
*What is running on the highest port?*
`apache`

---

## Task 2 - Compromising the machine

Now you've enumerated the machine, answer questions and compromise it!

## Answer the questions below
*Using GoBuster, find flag 1.*
`flag{f1rs7_fl4g}`
*Further enumerate the machine, what is flag 2?*
`flag{1m_s3c0nd_fl4g}`
*Crack the hash with easypeasy.txt, What is the flag 3?*
`flag{9fdafbd64c47471a8f54cd3fc64cd312}`
*What is the hidden directory?*
`/n0th1ng3ls3m4tt3r`
*Using the wordlist that provided to you in this task crack the hash. What is the password?*
`mypasswordforthatjob`
*What is the password to login to the machine via SSH?*
`iconvertedmypasswordtobinary`
*What is the user flag?*
`flag{n0wits33msn0rm4l}`
*What is the root flag?*
`flag{63a9f0ea7bb98050796b649e85481845}`
