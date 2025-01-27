# Looking Glass
Step through the looking glass. A sequel to the Wonderland challenge room.

https://tryhackme.com/room/lookingglass



# Answer the questions below

*Get the user flag*
`thm{65d3710e9d75d5f346d2bac669119a23}`
*Get the root flag*
`thm{bc2337b6f97d057b01da718ced6ead3f}`


# Timeline
1. Scan and only get dropbear
2. Realize im getting the msgs "lower" and "higher"
3. Find right port: *9150*
4. Get Jabberwocky poem
5. Decode poem, get creds
6. log in with creds

7. crontab will run writeable script as different user on restart + ive got perms to reboot as current user
8. revshell into script and reboot for new user
9. tweedledum has hashes, crack tehm with https://hashes.com/en/decrypt/hash
