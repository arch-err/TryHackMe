# Startup

Abuse traditional vulnerabilities via untraditional means.

(https://tryhackme.com/r/room/startup)[https://tryhackme.com/r/room/startup]

# Task 1 - Welcome to Spice Hut!

We are Spice Hut, a new startup company that just made it big! We offer a variety of spices and club sandwiches (in case you get hungry), but that is not why you are here. To be truthful, we aren't sure if our developers know what they are doing and our security concerns are rising. We ask that you perform a thorough penetration test and try to own root. Good luck!

## Answer the questions below
*What is the secret spicy soup recipe?*
`love`
*What are the contents of user.txt?*
`THM{03ce3d619b80ccbfb3b7fc81e46c0e79}`
*What are the contents of root.txt?*
`THM{f963aaa6a430f210222158ae15c3d76d}`



# Timeline
1. Enumerated, found anonymous ftp login and looted some files
2. Uploaded php-revshell to the ftps /ftp and executed through browser
3. Got shell, found recepies.txt
4. found /incidents folder with a pcap. Pcap contains bash-history where lennies password was recovered
5. Log in as lennie
6. Root seems to launch the writeable /etc/print.sh every min through cronjob. Edit print.sh to get revshell
7. Root! Done!
