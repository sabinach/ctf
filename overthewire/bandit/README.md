# Bandit

## XXX
Connect:```ssh banditXX@bandit.labs.overthewire.org -p 2220```      
Password:```XXX```

Problem:
- XXX

Solution:
```
XXX
```

Output:
```
XXX
```


## Level 0
Connect:```ssh bandit0@bandit.labs.overthewire.org -p 2220```      
Password:```bandit0```

Problem:
- The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.


##  Level 0 → Level 1
Connect:```ssh bandit0@bandit.labs.overthewire.org -p 2220```      
Password:```bandit0```

Problem:
- The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

Solution:
```
cat readme
```

Output:
```
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```


## Level 1 → Level 2
Connect:```ssh bandit1@bandit.labs.overthewire.org -p 2220```      
Password:```boJ9jbbUNNfktd78OOpsqOltutMc3MY1```

Problem:
- The password for the next level is stored in a file called - located in the home directory

Solution:
```
cat ./-
```

Output:
```
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```


## Level 2 → Level 3
Connect:```ssh bandit2@bandit.labs.overthewire.org -p 2220```      
Password:```CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9```

Problem:
- The password for the next level is stored in a file called spaces in this filename located in the home directory

Solution:
```
cat 'spaces in this filename'
```

Output:
```
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```


## Level 3 → Level 4
Connect:```ssh bandit3@bandit.labs.overthewire.org -p 2220```      
Password:```UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK```

Problem:
- The password for the next level is stored in a hidden file in the inhere directory.

Solution:
```
cd inhere
ls -a
cat .hidden
```

Output:
```
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```


## Level 4 → Level 5
Connect:```ssh bandit4@bandit.labs.overthewire.org -p 2220```      
Password:```pIwrPrtPN36QITSp3EQaw936yaFoFgAB```

Problem:
- The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Solution (Version 1 - manual):
```
cd inhere
**manually cat each file until I find one that is humanly-readable**
cat ./-file07
```

Solution (Version 2 - automated):
```
ssh bandit4@bandit.labs.overthewire.org -p 2220
file ./inhere/* | grep ASCII | awk -F: '{print $1}' | xargs cat
```

Output:
```
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```


## Level 5 → Level 6
Connect:```ssh bandit5@bandit.labs.overthewire.org -p 2220```      
Password:```koReBOKuIDDepwhWk7jZC0RTdopnAYKh```

Problem:
- The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    * human-readable
    * 1033 bytes in size
    * not executable

Solution:
```
find . -type f -size 1033c ! -executable -exec cat {} \;
```

Helpful Links:
- https://stackoverflow.com/questions/864316/how-to-pipe-list-of-files-returned-by-find-command-to-cat-to-view-all-the-files

Output:
```
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```


## Level 6 → Level 7
Connect:```ssh bandit6@bandit.labs.overthewire.org -p 2220```      
Password:```DXjZPULLxYr17uwoI01bNLQbtFemEgo7```

Problem:
- The password for the next level is stored somewhere on the server and has all of the following properties:
     * owned by user bandit7
     * owned by group bandit6
     * 33 bytes in size

Solution:
```
cd ..
find . -type f -size 33c -group bandit6 -user bandit7  -exec cat {} \;
```

Output:
```
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```


## Level 7 → Level 8
Connect:```ssh bandit7@bandit.labs.overthewire.org -p 2220```      
Password:```HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs```

Problem:
- The password for the next level is stored in the file data.txt next to the word millionth

Solution:
```
grep '^millionth' < data.txt | awk '{print $2}'
```

Output:
```
cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```


## Level 8 → Level 9
Connect:```ssh bandit8@bandit.labs.overthewire.org -p 2220```      
Password:```cvX2JJa4CFALtqS87jk27qwqGhBM9plV```

Problem:
- The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

Solution:
```
sort data.txt | uniq -u
```

Output:
```
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```


## Level 9 → Level 10
Connect:```ssh bandit9@bandit.labs.overthewire.org -p 2220```      
Password:```UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR```

Problem:
- The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

Solution:
```
strings data.txt | grep -E '=+'
```

Mistake:
```
strings data.txt | grep '^===*' | awk '{print $2}'
```

Output:
```
========== the*2i"4
=:G e
========== password
<I=zsGi
Z)========== is
A=|t&E
Zdb=
c^ LAh=3G
*SF=s
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
S=A.H&^
```


## Level 10 → Level 11
Connect:```ssh bandit10@bandit.labs.overthewire.org -p 2220```      
Password:```truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk```

Problem:
- The password for the next level is stored in the file data.txt, which contains base64 encoded data

Solution:
```
base64 -d data.txt
```

Output:
```
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```


## Level 11 → Level 12
Connect:```ssh bandit11@bandit.labs.overthewire.org -p 2220```      
Password:```IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR```

Problem:
- The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

Solution:
```
cat data.txt | tr '[a-zA-Z]' '[n-za-mN-ZA-M]'
```

Output:
```
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```


## Level 12 → Level 13
Connect:```ssh bandit12@bandit.labs.overthewire.org -p 2220```      
Password:```5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu```

Problem:
- The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

Solution:
```
mkdir /tmp/<username>
cp data.txt /tmp/<username>/data.txt
cd /tmp/<username>/data.txt

# reverse hex dump
xxd -r data.txt data

file data
>>> data: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
mv data data.gz
gzip -d data.gz

file data
>>> data: bzip2 compressed data, block size = 900k
mv data data.bz2
bzip2 -d data.bz2

file data
>>> data: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
mv data data.gz
gzip -d data.gz

file data
>>> data: POSIX tar archive (GNU)
mv data data.tar
tar -xvf data.tar
>>> data5.bin

file data5.bin
>>> data5.bin: POSIX tar archive (GNU)
mv data5.bin data5.tar
tar -xvf data5.tar
>>> data6.bin

file data6.bin
>>> data6.bin: bzip2 compressed data, block size = 900k
mv data6.bin data6.bz2
bzip2 -d data6.bz2

file data6
>>> data6: POSIX tar archive (GNU)
mv data6 data6.tar
tar -xvf data6.tar
>>> data8.bin

file data8.bin
>>> data8.bin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix
mv data8.bin data8.gz
gzip -d data8.gz

file data8
>>> data8: ASCII text

cat data8
```

Helpful Links:
- https://help.nexcess.net/77285-other/how-to-decompress-files-in-gzip
- https://superuser.com/questions/480950/how-to-decompress-a-bz2-file
- https://www.cyberciti.biz/faq/tar-extract-linux/
- 

Output:
```
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```


## Level 13 → Level 14
Connect:```ssh bandit13@bandit.labs.overthewire.org -p 2220```      
Password:```8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL```

Problem:
- The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on

Solution:
```
ls
>>> sshkey.private

ssh -i sshkey.private bandit14@localhost
>>> The authenticity of host 'localhost (127.0.0.1)' can't be established.
>>> ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
>>> Are you sure you want to continue connecting (yes/no)? yes

# now in bandit14@bandit
cat /etc/bandit_pass/bandit14
```

Helpful Links:
- https://support.rackspace.com/how-to/logging-in-with-an-ssh-private-key-on-linuxmac/

Output:
```
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```


## Level 14 → Level 15
Connect:```ssh bandit14@bandit.labs.overthewire.org -p 2220```      
Password:```4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e```

Problem:
- The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

Solution:
```
nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

Output:
```
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```


## Level 15 → Level 16
Connect:```ssh bandit15@bandit.labs.overthewire.org -p 2220```      
Password:```BfMYroe26WYalil77FoDi9qh59eK5xNr```

Problem:
- The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.
- Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

Solution:
```
openssl s_client -connect localhost:30001
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

Helpful Links:
- https://www.misterpki.com/openssl-s-client/
- The OpenSSL command line tool can be used for several purposes like creating certificates, viewing certificates and testing https services/connectivity etc. This document provides a summary of "openssl s_client" commands which can be used to test connectivity to SSL services.

Output:
```
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd
```


## Level 16 → Level 17
Connect:```ssh bandit16@bandit.labs.overthewire.org -p 2220```      
Password:```cluFn7wTiGryunymYOu4RcffSxQluehd```

Problem:
- The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

Solution:
```
nmap -sV --script ssl-cert -p 31000-32000 localhost
```
```
>>>
Starting Nmap 7.40 ( https://nmap.org ) at 2020-09-07 06:52 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00030s latency).
Not shown: 996 closed ports
PORT      STATE SERVICE     VERSION
31046/tcp open  echo
31518/tcp open  ssl/echo
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2020-07-11T13:58:02
| Not valid after:  2021-07-11T13:58:02
| MD5:   a536 6d53 0934 a53b 7955 4dab ddef b472
|_SHA-1: cade ac3f e416 7f17 489a 3336 b411 e0c8 2a3b 6d37
31691/tcp open  echo
31790/tcp open  ssl/unknown
| fingerprint-strings:
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq:
|_    Wrong! Please enter the correct current password
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Issuer: commonName=localhost
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2020-09-03T20:17:26
| Not valid after:  2021-09-03T20:17:26
| MD5:   ed95 0532 bb94 7ace d607 d759 1266 8ca9
|_SHA-1: ce79 d7d1 880b b63e 01fb 2f56 9fe3 e3a9 6590 986a
31960/tcp open  echo
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=9/7%Time=5F55BC83%P=x86_64-pc-linux-gn
SF:u%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cur
SF:rent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20the\
SF:x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Pleas
SF:e\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest,3
SF:1,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n
SF:")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x2
SF:0password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x20c
SF:orrect\x20current\x20password\n")%r(TLSSessionReq,31,"Wrong!\x20Please\
SF:x20enter\x20the\x20correct\x20current\x20password\n")%r(Kerberos,31,"Wr
SF:ong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%r(
SF:FourOhFourRequest,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cu
SF:rrent\x20password\n")%r(LPDString,31,"Wrong!\x20Please\x20enter\x20the\
SF:x20correct\x20current\x20password\n")%r(LDAPSearchReq,31,"Wrong!\x20Ple
SF:ase\x20enter\x20the\x20correct\x20current\x20password\n")%r(SIPOptions,
SF:31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\
SF:n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 88.02 seconds
<<<
```
```
openssl s_client -connect localhost:31790
cluFn7wTiGryunymYOu4RcffSxQluehd
```

Output:
```
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```


## Level 17 → Level 18
Connect/Password:
```
# create file with ssh private key
vim level17-sshkey.private
**copy RSA private key (output found from level 16) into this file, then exit file**
chmod 600 level17-sshkey.private

# login
ssh -i level17-sshkey.private bandit17@bandit.labs.overthewire.org -p 2220
```

Problem:
- There are 2 files in the homedirectory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new
- NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19

Solution:
```
diff passwords.old passwords.new
```

Helpful Links:
- https://support.rackspace.com/how-to/logging-in-with-an-ssh-private-key-on-linuxmac/

Output:
```
42c42
< w0Yfolrc5bwjS4qw5mq1nnQi6mF03bii
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```


## Level 18 → Level 19
Connect:```ssh bandit18@bandit.labs.overthewire.org -p 2220```      
Password:```kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd```

Problem:
- The password for the next level is stored in a file readme in the homedirectory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

Solution:
```
# Force pseudo-tty allocation. This can be used to execute arbitrary screen-based programs on a remote machine, which can be very useful
ssh -t bandit18@bandit.labs.overthewire.org -p 2220 /bin/sh
kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd

cat readme
```

Output:
```
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```


## Level 19 → Level 20
Connect:```ssh bandit19@bandit.labs.overthewire.org -p 2220```      
Password:```IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x```

Problem:
- To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

Solution (Version 1):
```
file bandit20-do
>>> bandit20-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8e941f24b8c5cd0af67b22b724c57e1ab92a92a1, not stripped

./bandit20-do
>>> Run a command as another user. 
>>> Example: ./bandit20-do id

./bandit20-do id
>>> uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)

# notice that owner of bandit20-do is bandit20 (and group is bandit19)
ls -l
-rwsr-x--- 1 bandit20 bandit19 7296 May  7 20:14 bandit20-do

./bandit20-do cat /etc/bandit_pass/bandit20
```

Output:
```
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```


## Level 20 → Level 21
Connect:```ssh bandit20@bandit.labs.overthewire.org -p 2220```      
Password:```GbKksEFF4yrVs6il55v6gwY5aVje5f0j```

Problem:
- There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).
- NOTE: Try connecting to your own network daemon to see if it works as you think

Solution:
```
file suconnect
>>> suconnect: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=74c0f6dc184e0412b6dc52e542782f43807268e1, not stripped

# notice that owner of suconnect is bandit21 (and group is bandit20)
ls -l suconnect
>>> -rwsr-x--- 1 bandit21 bandit20 12088 May  7 20:14 suconnect

./suconnect
>>> Usage: ./suconnect <portnumber>
>>> This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.

XXXXXXXXX TBD XXXXXXXXX 
```

Mistake:
```
nmap localhost
>>>
Starting Nmap 7.40 ( https://nmap.org ) at 2020-09-07 07:43 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00024s latency).
Not shown: 997 closed ports
PORT      STATE SERVICE
22/tcp    open  ssh
113/tcp   open  ident
30000/tcp open  ndmps
Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
<<<

./suconnect 22 GbKksEFF4yrVs6il55v6gwY5aVje5f0j
>>> Read: SSH-2.0-OpenSSH_7.4p1
>>> ERROR: This doesn't match the current password!
```

Output:
```
XXX
```


