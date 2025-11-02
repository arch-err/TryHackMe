# Silver Platter
Can you breach the server?

(https://tryhackme.com/r/room/silverplatter)[https://tryhackme.com/r/room/silverplatter]

#  Task 1 -  Silver Platter

Think you've got what it takes to outsmart the Hack Smarter Security team? They claim to be unbeatable, and now it's your chance to prove them wrong. Dive into their web server, find the hidden flags, and show the world your elite hacking skills. Good luck, and may the best hacker win!

But beware, this won't be a walk in the digital park. Hack Smarter Security has fortified the server against common attacks and their password policy requires passwords that have not been breached (they check it against the rockyou.txt wordlist - that's how 'cool' they are). The hacking gauntlet has been thrown, and it's time to elevate your game. Remember, only the most ingenious will rise to the top.

May your code be swift, your exploits flawless, and victory yours!

Make sure you wait a full 5 minutes after you start the machine before scanning or doing any enumeration. This will make sure all the services have started.

## Answer the questions below
*What is the user flag?*
`THM{c4ca4238a0b923820dcc509a6f75849b}`
*What is the root flag?*
``

# Notes
- nginx/1.18.0 (Ubuntu)
- nmap
    ```
    22/tcp   open  ssh
    80/tcp   open  http
    8080/tcp open  http-proxy
    ```
- `http://10.10.165.55:8080/website/` returns "forbidden"
- `http://10.10.165.55:8080/silverpeas/` returns the silverpeas webapp





# Timeline
1. Enum (nmap, ferox)
2. Finds a username and talk about a site called "silverpeas"
3. Find silverpeas website, try to log in with the found username
4. The description says that i can't use existing wordlists, so let's `cewl` the main site
5. Using a caido + automation I bruteforce passwords and find the correct password
6. Soo, while googling for Silverpeas CVEs I found this:
