# GamingServer
An Easy Boot2Root box for beginners

[https://tryhackme.com/room/gamingserver](https://tryhackme.com/room/gamingserver)

# Task 1 - Boot2Root

Can you gain access to this gaming server built by amateurs with no experience of web development and take advantage of the deployment system.

## Answer the questions below
*What is the user flag?*
`a5c2ff8b9c2e3d4fe9d4ff2f1a5a6e7e`
*What is the root flag?*
`2e337b8c9f3aff0c2b3e8d4e6a7c88fc`


# Timeline
1. Enum and loot webpage
2. Found ssh key and dictionary of passwords, found reference in a comment to user "john"
3. crack ssh key passphrase with dict
4. log in as john
5. john is a member of the lxc group
6. lxd container breakout privesc (https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation)
7. Follow instructions above
8. I get bad shell and env in the container
9. Persistence via authorized keys
10. SSH as root
