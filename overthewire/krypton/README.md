# Krypton

##  Level 0 → Level 1
Problem:
- Welcome to Krypton! The first level is easy. The following string encodes the password using Base64: ```S1JZUFRPTklTR1JFQVQ=```. Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/

Solution:
```
https://www.base64decode.org/
```

Output:
```
KRYPTONISGREAT
```


---


##  Level 1 → Level 2
Connect: ```ssh krypton1@krypton.labs.overthewire.org  -p 2231```      
Password: ```KRYPTONISGREAT```

Problem:
- The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

Solution:
```
cd /krypton/krypton1
cat README
>>>
Welcome to Krypton! This game is intended to give hands on experience with cryptography and cryptanalysis.  The levels progress from classic ciphers, to modern, easy to harder. Although there are excellent public tools, like cryptool, to perform the simple analysis, we strongly encourage you to try and do these without them for now.  We will use them in later exercises. ** Please try these levels without cryptool first **
<<<
```
```
cat krypton2
>>> YRIRY GJB CNFFJBEQ EBGGRA

# ON PERSONAL MACHINE:
./caesar_cipher.py "YRIRY GJB CNFFJBEQ EBGGRA"

# shift 13 is the only text that makes sense
```

Output:
```
LEVEL TWO PASSWORD ROTTEN
```


---


##  Level 2 → Level 3
Connect: ```ssh krypton2@krypton.labs.overthewire.org  -p 2231```      
Password: ```ROTTEN```

Problem:
[lvl2-3.png](https://github.com/sabinach/ctf/tree/master/overthewire/krypton/lvl2-3.png)

Solution:
```
cd /krypton/krypton2
cat krypton3
>>> OMQEMDUEQMEK

# ON PERSONAL MACHINE:
./caesar_cipher.py OMQEMDUEQMEK

# shift 14 is the only text that makes sense
```

Output:
```
CAESARISEASY
```


---


##  Level 3 → Level 4
Connect: ```ssh krypton3@krypton.labs.overthewire.org  -p 2231```      
Password: ```CAESARISEASY```

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


---


##  Level 4 → Level 5
Connect: ```ssh krypton4@krypton.labs.overthewire.org  -p 2231```      
Password: ```XXX```

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


---


##  Level 5 → Level 6
Connect: ```ssh krypton5@krypton.labs.overthewire.org  -p 2231```      
Password: ```XXX```

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


---


##  Level 6 → Level 7
Connect: ```ssh krypton6@krypton.labs.overthewire.org  -p 2231```      
Password: ```XXX```

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
