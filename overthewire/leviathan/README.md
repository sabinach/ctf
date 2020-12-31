# Leviathan

##  Level 0
Connect: ```ssh leviathan0@leviathan.labs.overthewire.org  -p 2223```      
Password: ```leviathan0```

Problem:
- There is no information for this level, intentionally.

Solution:
```
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
ltrace ./check
>>>
__libc_start_main(0x804853b, 1, 0xffffd724, 0x8048610 <unfinished ...>
printf("password: ")                                       = 10
getchar(1, 0, 0x65766f6c, 0x646f6700password: q
)                      = 113
getchar(1, 0, 0x65766f6c, 0x646f6700)        = 10
getchar(1, 0, 0x65766f6c, 0x646f6700q
)                      = 113
strcmp("q\nq", "sex")                                     = -1
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

Mistake:
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
XXX
```

Output:
```
XXX
```


---


##  Level 2 → Level 3
Connect: ```ssh leviathan3@leviathan.labs.overthewire.org  -p 2223```      
Password: ```XXX```

Problem:
- There is no information for this level, intentionally.

Solution:
```
XXX
```

Output:
```
XXX
```


---


##  Level 3 → Level 4
Connect: ```ssh leviathan4@leviathan.labs.overthewire.org  -p 2223```      
Password: ```XXX```

Problem:
- There is no information for this level, intentionally.

Solution:
```
XXX
```

Output:
```
XXX
```


---


##  Level 4 → Level 5
Connect: ```ssh leviathan5@leviathan.labs.overthewire.org  -p 2223```      
Password: ```XXX```

Problem:
- There is no information for this level, intentionally.

Solution:
```
XXX
```

Output:
```
XXX
```


---


##  Level 5 → Level 6
Connect: ```ssh leviathan6@leviathan.labs.overthewire.org  -p 2223```      
Password: ```XXX```

Problem:
- There is no information for this level, intentionally.

Solution:
```
XXX
```

Output:
```
XXX
```


---


##  Level 6 → Level 7
Connect: ```ssh leviathan7@leviathan.labs.overthewire.org  -p 2223```      
Password: ```XXX```

Problem:
- There is no information for this level, intentionally.

Solution:
```
XXX
```

Output:
```
XXX
```


