# Bandit

## XXX
Connect:```XXX```      
Password:```XXX```

Problem:
- XXX

Solution:
```
XXX
```

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
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

Password Found:
```
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```


## Level 9 → Level 10
Connect:```ssh bandit9@bandit.labs.overthewire.org -p 2220```      
Password:```truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk```

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

Password Found:
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


## XXX
Connect:```XXX```      
Password:```XXX```

Problem:
- XXX

Solution:
```
XXX
```

Password Found:
```
XXX
```

