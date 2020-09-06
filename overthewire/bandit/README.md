# Bandit

## XXX
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
Problem:
- The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

Solution:
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

Password Given:
```
bandit0
```


##  Level 0 → Level 1
Problem:
- The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

Solution:
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
cat readme
```

Password Found:
```
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```


## Level 1 → Level 2
Problem:
- The password for the next level is stored in a file called - located in the home directory

Solution:
```
ssh bandit1@bandit.labs.overthewire.org -p 2220
cat ./-
```

Password Found:
```
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```


## Level 2 → Level 3
Problem:
- The password for the next level is stored in a file called spaces in this filename located in the home directory

Solution:
```
ssh bandit2@bandit.labs.overthewire.org -p 2220
cat 'spaces in this filename'
```

Password Found:
```
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```


## Level 3 → Level 4
Problem:
- The password for the next level is stored in a hidden file in the inhere directory.

Solution:
```
ssh bandit3@bandit.labs.overthewire.org -p 2220
cd inhere
ls -a
cat .hidden
```

Password Found:
```
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```


## Level 4 → Level 5
Problem:
- The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

Solution (Version 1 - manual):
```
ssh bandit4@bandit.labs.overthewire.org -p 2220
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
Problem:
- The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
    * human-readable
    * 1033 bytes in size
    * not executable

Solution:
```
ssh bandit5@bandit.labs.overthewire.org -p 2220
find . -type f -size 1033c ! -executable -exec cat {} \;
```

Helpful Links:
- https://stackoverflow.com/questions/864316/how-to-pipe-list-of-files-returned-by-find-command-to-cat-to-view-all-the-files

Password Found:
```
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```


## Level 6 → Level 7
Problem:
- The password for the next level is stored somewhere on the server and has all of the following properties:
     * owned by user bandit7
     * owned by group bandit6
     * 33 bytes in size

Solution:
```
XXX
```

Password Found:
```
XXX
```




