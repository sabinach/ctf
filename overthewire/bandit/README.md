# Bandit

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
mkdir /tmp/<username12>
cp data.txt /tmp/<username12>/data.txt
cd /tmp/<username12>/data.txt

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

# [terminal 1] create port listener
nc -l -p 31337

# [terminal 2] connect to port via suconnect
./suconnect 31337

# [terminal 1] submit password
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
>>> gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr

# [terminal 2] receive and send new password
>>> Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
>>> Password matches, sending next password
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

Helpful Links:
- https://www.youtube.com/watch?v=EmWV9rIU2oQ&ab_channel=Firewalls.com
- Local Test:
     * ```nc -l -p 31337``` [terminal 1]
     * ```nc localhost 31337```  [terminal 2]

Output:
```
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```


## Level 21 → Level 22
Connect:```ssh bandit21@bandit.labs.overthewire.org -p 2220```      
Password:```gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr```

Problem:
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

Solution:
```
cd /etc/cron.d
ls

cat cronjob_bandit22
>>> @reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
>>> * * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
```
```
cat /usr/bin/cronjob_bandit22.sh
>>> 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
<<<
```
```
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```

Output:
```
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```


## Level 22 → Level 23
Connect:```ssh bandit22@bandit.labs.overthewire.org -p 2220```      
Password:```Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI```

Problem:
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
- NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

Solution:
```
cd /etc/cron.d
ls

cat cronjob_bandit23
>>> @reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
>>> * * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
```
```
cat /usr/bin/cronjob_bandit23.sh
>>>
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget
<<<
```
```
cd /usr/bin
./cronjob_bandit23.sh
>>> Copying passwordfile /etc/bandit_pass/bandit22 to /tmp/8169b67bd894ddbb4412f91573b38db3

# this shows THIS level's password, not the next level's!
cat /tmp/8169b67bd894ddbb4412f91573b38db3
>>> Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI

# literally just copy the script into terminal, but change myname
myname=bandit23
echo I am user $myname | md5sum | cut -d ' ' -f 1
>>> 8ca319486bfbbc3663ea0fbe81326349

cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```

Output:
```
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```


## Level 23 → Level 24
Connect:```ssh bandit23@bandit.labs.overthewire.org -p 2220```      
Password:```jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n```

Problem:
- A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.
- NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!
- NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

Solution:
```
cd /etc/cron.d
ls

cat cronjob_bandit24
>>> @reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
>>> * * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
```
```
cat /usr/bin/cronjob_bandit24.sh
>>>
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
<<<
```
```
cd /usr/bin
./cronjob_bandit24.sh
>>>
...
Handling pycompile
rm: cannot remove './pycompile': Permission denied
Handling pydoc
rm: cannot remove './pydoc': Permission denied
Handling pydoc2.7
rm: cannot remove './pydoc2.7': Permission denied
Handling pydoc3
rm: cannot remove './pydoc3': Permission denied
Handling pydoc3.5
rm: cannot remove './pydoc3.5': Permission denied
Handling pygettext
rm: cannot remove './pygettext': Permission denied
Handling pygettext2.7
...
<<<
```
```
ls -al /usr/bin/cronjob_bandit24.sh
>>> -rwxr-x--- 1 bandit24 bandit23 376 May 14 09:41 /usr/bin/cronjob_bandit24.sh

cd /var/spool
ls -l
>>> bandit24  cron  mail  rsyslog

cd bandit24
ls
>>> ls: cannot open directory '.': Permission denied

cd  /var/spool
ls -l
>>> drwxrwx-wx 40 root bandit24 4096 Sep  7 21:48 bandit24

mkdir /tmp/<username23>
cd /tmp/<username23>

touch getPassword24.sh
chmod +x getPassword24.sh
vim getPassword24.sh

touch password24.txt
chmod 666 password24.txt
```
```
# write the following lines of code into getPassword24.sh 
>>>
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/sallycolly2/password24.txt
<<<
```
```
cp getPassword24.sh /var/spool/bandit24/getPassword24.sh
ls -al /var/spool/bandit24/getPassword24.sh
>>> -rwxr-xr-x 1 bandit23 bandit23 76 Sep  7 21:45 /var/spool/bandit24/getPassword24.sh

(wait 60 sec)

cat password24.txt
```

Output:
```
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```


## Level 24 → Level 25
Connect:```ssh bandit24@bandit.labs.overthewire.org -p 2220```      
Password:```UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ```

Problem:
- A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

Solution:
```
nc localhost 30002
>>> I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ 0001
>>> Wrong! Please enter the correct pincode. Try again.

mkdir /tmp/<username24>
cd /tmp/<username24>

touch getPassword25.sh
chmod +x getPassword25.sh
vim getPassword25.sh

touch output.txt
```
```
# write the following lines of code into getPassword25.sh 
>>>
#!/bin/bash

password24="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for pin in {0000..9999}
do
    echo "$password24 $pin"
done | nc localhost 30002 > output.txt

cat output.txt | grep -v "Wrong"
<<<
```
```
./getPassword25.sh
```

Output:
```
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
Exiting.
```


## Level 25 → Level 26
Connect:```ssh bandit25@bandit.labs.overthewire.org -p 2220```      
Password:```uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG```

Problem:
- Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

Solution:
```
cat bandit26.sshkey
>>>
-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEApis2AuoooEqeYWamtwX2k5z9uU1Afl2F8VyXQqbv/LTrIwdW
pTfaeRHXzr0Y0a5Oe3GB/+W2+PReif+bPZlzTY1XFwpk+DiHk1kmL0moEW8HJuT9
/5XbnpjSzn0eEAfFax2OcopjrzVqdBJQerkj0puv3UXY07AskgkyD5XepwGAlJOG
xZsMq1oZqQ0W29aBtfykuGie2bxroRjuAPrYM4o3MMmtlNE5fC4G9Ihq0eq73MDi
1ze6d2jIGce873qxn308BA2qhRPJNEbnPev5gI+5tU+UxebW8KLbk0EhoXB953Ix
3lgOIrT9Y6skRjsMSFmC6WN/O7ovu8QzGqxdywIDAQABAoIBAAaXoETtVT9GtpHW
qLaKHgYtLEO1tOFOhInWyolyZgL4inuRRva3CIvVEWK6TcnDyIlNL4MfcerehwGi
il4fQFvLR7E6UFcopvhJiSJHIcvPQ9FfNFR3dYcNOQ/IFvE73bEqMwSISPwiel6w
e1DjF3C7jHaS1s9PJfWFN982aublL/yLbJP+ou3ifdljS7QzjWZA8NRiMwmBGPIh
Yq8weR3jIVQl3ndEYxO7Cr/wXXebZwlP6CPZb67rBy0jg+366mxQbDZIwZYEaUME
zY5izFclr/kKj4s7NTRkC76Yx+rTNP5+BX+JT+rgz5aoQq8ghMw43NYwxjXym/MX
c8X8g0ECgYEA1crBUAR1gSkM+5mGjjoFLJKrFP+IhUHFh25qGI4Dcxxh1f3M53le
wF1rkp5SJnHRFm9IW3gM1JoF0PQxI5aXHRGHphwPeKnsQ/xQBRWCeYpqTme9amJV
tD3aDHkpIhYxkNxqol5gDCAt6tdFSxqPaNfdfsfaAOXiKGrQESUjIBcCgYEAxvmI
2ROJsBXaiM4Iyg9hUpjZIn8TW2UlH76pojFG6/KBd1NcnW3fu0ZUU790wAu7QbbU
i7pieeqCqSYcZsmkhnOvbdx54A6NNCR2btc+si6pDOe1jdsGdXISDRHFb9QxjZCj
6xzWMNvb5n1yUb9w9nfN1PZzATfUsOV+Fy8CbG0CgYEAifkTLwfhqZyLk2huTSWm
pzB0ltWfDpj22MNqVzR3h3d+sHLeJVjPzIe9396rF8KGdNsWsGlWpnJMZKDjgZsz
JQBmMc6UMYRARVP1dIKANN4eY0FSHfEebHcqXLho0mXOUTXe37DWfZza5V9Oify3
JquBd8uUptW1Ue41H4t/ErsCgYEArc5FYtF1QXIlfcDz3oUGz16itUZpgzlb71nd
1cbTm8EupCwWR5I1j+IEQU+JTUQyI1nwWcnKwZI+5kBbKNJUu/mLsRyY/UXYxEZh
ibrNklm94373kV1US/0DlZUDcQba7jz9Yp/C3dT/RlwoIw5mP3UxQCizFspNKOSe
euPeaxUCgYEAntklXwBbokgdDup/u/3ms5Lb/bm22zDOCg2HrlWQCqKEkWkAO6R5
/Wwyqhp/wTl8VXjxWo+W+DmewGdPHGQQ5fFdqgpuQpGUq24YZS8m66v5ANBwd76t
IZdtF5HXs2S5CADTwniUS5mX1HO9l5gUkk+h0cH5JnPtsMCnAUM+BRY=
-----END RSA PRIVATE KEY-----
<<<
```
```
# ON PERSONAL COMPUTER (not on bandit25 server)
# create file with ssh private key
vim level26-sshkey.private
**copy RSA private key (output found from level 16) into this file, then exit file**
chmod 600 level26-sshkey.private

# login (it will kick us right back out)
ssh bandit26@bandit.labs.overthewire.org -p 2220 -i level26-sshkey.private
>>> Connection to bandit.labs.overthewire.org closed.
```
```
# ON BANDIT25 SERVER
cd /etc
cat passwd
>>>
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/bin/false
messagebus:x:101:104::/var/run/dbus:/bin/false
sshd:x:102:65534::/run/sshd:/usr/sbin/nologin
identd:x:103:65534::/var/run/identd:/bin/false
ntp:x:104:107::/home/ntp:/bin/false
bandit0:x:11000:11000:bandit level 0:/home/bandit0:/bin/bash
bandit1:x:11001:11001:bandit level 1:/home/bandit1:/bin/bash
bandit2:x:11002:11002:bandit level 2:/home/bandit2:/bin/bash
bandit3:x:11003:11003:bandit level 3:/home/bandit3:/bin/bash
bandit4:x:11004:11004:bandit level 4:/home/bandit4:/bin/bash
bandit5:x:11005:11005:bandit level 5:/home/bandit5:/bin/bash
bandit6:x:11006:11006:bandit level 6:/home/bandit6:/bin/bash
bandit7:x:11007:11007:bandit level 7:/home/bandit7:/bin/bash
bandit8:x:11008:11008:bandit level 8:/home/bandit8:/bin/bash
bandit9:x:11009:11009:bandit level 9:/home/bandit9:/bin/bash
bandit10:x:11010:11010:bandit level 10:/home/bandit10:/bin/bash
bandit11:x:11011:11011:bandit level 11:/home/bandit11:/bin/bash
bandit12:x:11012:11012:bandit level 12:/home/bandit12:/bin/bash
bandit13:x:11013:11013:bandit level 13:/home/bandit13:/bin/bash
bandit14:x:11014:11014:bandit level 14:/home/bandit14:/bin/bash
bandit15:x:11015:11015:bandit level 15:/home/bandit15:/bin/bash
bandit16:x:11016:11016:bandit level 16:/home/bandit16:/bin/bash
bandit17:x:11017:11017:bandit level 17:/home/bandit17:/bin/bash
bandit18:x:11018:11018:bandit level 18:/home/bandit18:/bin/bash
bandit19:x:11019:11019:bandit level 19:/home/bandit19:/bin/bash
bandit20:x:11020:11020:bandit level 20:/home/bandit20:/bin/bash
bandit21:x:11021:11021:bandit level 21:/home/bandit21:/bin/bash
bandit22:x:11022:11022:bandit level 22:/home/bandit22:/bin/bash
bandit23:x:11023:11023:bandit level 23:/home/bandit23:/bin/bash
bandit24:x:11024:11024:bandit level 24:/home/bandit24:/bin/bash
bandit25:x:11025:11025:bandit level 25:/home/bandit25:/bin/bash
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit27:x:11027:11027:bandit level 27:/home/bandit27:/bin/bash
bandit28:x:11028:11028:bandit level 28:/home/bandit28:/bin/bash
bandit29:x:11029:11029:bandit level 29:/home/bandit29:/bin/bash
bandit30:x:11030:11030:bandit level 30:/home/bandit30:/bin/bash
bandit31:x:11031:11031:bandit level 31:/home/bandit31:/bin/bash
bandit32:x:11032:11032:bandit level 32:/home/bandit32:/home/bandit32/uppershell
bandit33:x:11033:11033:bandit level 33:/home/bandit33:/bin/bash
bandit27-git:x:11527:11527::/home/bandit27-git:/usr/bin/git-shell
bandit28-git:x:11528:11528::/home/bandit28-git:/usr/bin/git-shell
bandit29-git:x:11529:11529::/home/bandit29-git:/usr/bin/git-shell
bandit30-git:x:11530:11530::/home/bandit30-git:/usr/bin/git-shell
bandit31-git:x:11531:11531::/home/bandit31-git:/usr/bin/git-shell
<<<
```
```
cat /usr/bin/showtext
>>>
#!/bin/sh
export TERM=linux
more ~/text.txt
exit 0
<<<
```
```
# ON PERSONAL COMPUTER (not on bandit25 server)
**make terminal as small as possible so that we can access the "more" command (make sure that not everything in ~/text.txt can fit on your terminal screen)**

# open vim editor
v

# access the bandit26 password
:e /etc/bandit_pass/bandit26
>>> 5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

# exit file
:q

# go back to vim
v

# set shell type
:set shell=/bin/bash
:shell
```

Output:
```
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
```


## Level 26 → Level 27
Connect/Password:
```
# ON PERSONAL COMPUTER (not on bandit25 server)

# create file with ssh private key
vim level26-sshkey.private
**copy RSA private key (output found from level 16) into this file, then exit file**
chmod 600 level26-sshkey.private

**make terminal as small as possible so that we can access the "more" command (make sure that not everything in ~/text.txt can fit on your terminal screen)**
ssh bandit26@bandit.labs.overthewire.org -p 2220 -i level26-sshkey.private

# open vim editor
v

# set shell type
:set shell=/bin/bash
:shell
```

Problem:
- Good job getting a shell! Now hurry and grab the password for bandit27!

Solution:
```
file bandit27-do
>>> bandit27-do: setuid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=8e941f24b8c5cd0af67b22b724c57e1ab92a92a1, not stripped

./bandit27-do
>>> Run a command as another user.
>>> Example: ./bandit27-do id

./bandit27-do id
>>> uid=11026(bandit26) gid=11026(bandit26) euid=11027(bandit27) groups=11026(bandit26)

# notice that owner of bandit27-do is bandit27 (and group is bandit26)
ls -l
-rwsr-x--- 1 bandit27 bandit26 7296 May  7 20:14 bandit27-do

./bandit27-do cat /etc/bandit_pass/bandit27
```

Output:
```
3ba3118a22e93127a4ed485be72ef5ea
```


## Level 27 → Level 28
Connect:```ssh bandit27@bandit.labs.overthewire.org -p 2220```      
Password:```3ba3118a22e93127a4ed485be72ef5ea```

Problem:
- There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27.
- Clone the repository and find the password for the next level.

Solution:
```
mkdir /tmp/<username27>
cd /tmp/<username27>

git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
yes
3ba3118a22e93127a4ed485be72ef5ea

cd repo
cat README
```

Output:
```
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```


## Level 28 → Level 29
Connect:```ssh bandit28@bandit.labs.overthewire.org -p 2220```      
Password:```0ef186ac70e04ea33b4c1853d2526fa2```

Problem:
- There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.
- Clone the repository and find the password for the next level.

Solution:
```
mkdir /tmp/<username28>
cd /tmp/<username28>

git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
yes
0ef186ac70e04ea33b4c1853d2526fa2
```
```
cd repo
cat README.md
>>>
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx
<<<
```
```
git log -p
```

Output:
```
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

diff --git a/README.md b/README.md
index 3f7cee8..5c6457b 100644
--- a/README.md
+++ b/README.md
@@ -4,5 +4,5 @@ Some notes for level29 of bandit.
 ## credentials

 - username: bandit29
-- password: bbc96594b4e001778eee9975372716b2
+- password: xxxxxxxxxx
```


## Level 29 → Level 30
Connect:```ssh bandit29@bandit.labs.overthewire.org -p 2220```      
Password:```bbc96594b4e001778eee9975372716b2```

Problem:
- There is a git repository at ssh://bandit29-git@localhost/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29.
- Clone the repository and find the password for the next level.

Solution:
```
mkdir /tmp/<username29>
cd /tmp/<username29>

git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
yes
bbc96594b4e001778eee9975372716b2
```
```
cd repo
cat README.md
>>>
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>
<<<
```
```
git branch
>>> * master

git branch -a
>>>
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/dev
  remotes/origin/master
  remotes/origin/sploits-dev
<<<

git checkout origin/dev
cat README.md
```

Output:
```
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf 
```


## Level 30 → Level 31
Connect:```ssh bandit30@bandit.labs.overthewire.org -p 2220```      
Password:```5b90576bedb2cc04c86a9e924ce42faf```

Problem:
- There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.a
- Clone the repository and find the password for the next level.

Solution:
```
mkdir /tmp/<username30>
cd /tmp/<username30>

git clone ssh://bandit30-git@localhost/home/bandit30-git/repo
yes
5b90576bedb2cc04c86a9e924ce42faf

cd repo
cat README.md
>>> just an epmty file... muahaha
```
```
# extremely troll: "Ben Dover".. "noone" lol 
git log
>>>
commit 3aefa229469b7ba1cc08203e5d8fa299354c496b
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:54 2020 +0200

    initial commit of README.md
<<<
```
```
cd .git
cat packed-refs
>>>
# pack-refs with: peeled fully-peeled
3aefa229469b7ba1cc08203e5d8fa299354c496b refs/remotes/origin/master
f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea refs/tags/secret 
<<<
```
```
# this doesn't do anything sigh....
git fetch origin tag secret
yes
5b90576bedb2cc04c86a9e924ce42faf

# shows associated commit
git show secret
```

Output:
```
47e603bb428404d265f59c42920d81e5
```


## Level 31 → Level 32
Connect:```ssh bandit31@bandit.labs.overthewire.org -p 2220```      
Password:```47e603bb428404d265f59c42920d81e5```

Problem:
- There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.
- Clone the repository and find the password for the next level.

Solution:
```
mkdir /tmp/<username31>
cd /tmp/<username31>

git clone ssh://bandit31-git@localhost/home/bandit31-git/repo
yes
47e603bb428404d265f59c42920d81e5
```
```
cd repo
cat README.md
>>>
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master
<<<
```
```
# add the following to key.txt
vim key.txt
>>> May I come in?

vim .gitignore
**remove *.txt**

git add .
git commit -m "added key.txt"
git push
yes
47e603bb428404d265f59c42920d81e5
```

Output:
```
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 56a9bf19c63d650ce78e6ec0354ee45e
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
To ssh://localhost/home/bandit31-git/repo
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'ssh://bandit31-git@localhost/home/bandit31-git/repo'
```


## Level 32 → Level 33
Connect:```ssh bandit32@bandit.labs.overthewire.org -p 2220```      
Password:```56a9bf19c63d650ce78e6ec0354ee45e```

Problem:
- After all this git stuff its time for another escape. Good luck!

Solution:
```
# shown at login
>>>WELCOME TO THE UPPERCASE SHELL

ls
>>> sh: 1: LS: not found

# switch to bash (no letters needed, so no conversion!)
$0

# so basically echo'ing $0 will produce "sh" (not uppercase), which will force the shell to accept the command, and switch us to the regular sh bash
echo $0
>>> sh

cat /etc/bandit_pass/bandit33
```

Mistake:
```
ls='ls'
"$ls"
>>> sh: 1: : Permission denied

cd='cat /etc/bandit_pass/bandit32'
"$cd"
>>> sh: 1: : Permission denied
```

Helpful Links:
- https://bash.cyberciti.biz/guide/$0
- https://unix.stackexchange.com/questions/444946/how-can-we-run-a-command-stored-in-a-variable
- https://www.cyberciti.biz/faq/linux-unix-shell-programming-converting-lowercase-uppercase/

Output:
```
c9c3199ddf4121b10cf581a98d51caee
```


## Level 33 → Level 34
Connect:```ssh bandit33@bandit.labs.overthewire.org -p 2220```      
Password:```c9c3199ddf4121b10cf581a98d51caee```

Problem:
- At this moment, level 34 does not exist yet.

Solution:
```
cat README.txt
```

Output:
```
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
```

---

# Template
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
