# General Skills

## 50 - 2Warm
Problem:
- Can you convert number 42 (base 10) to binary (base 2)?

Solution:
- Convert base 10 to base 2 using http://www.unitconversion.org/numbers/base-10-to-base-2-conversion.html

Flag:
```
picoCTF{101010}
```


## 50 - Lets Warm Up
Problem:
- If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

Solution:
- Use ascii table: http://www.asciitable.com/

Flag:
```
picoCTF{p}
``` 


## 50 - Warmed Up
Problem:
- What is 0x3D (base 16) in decimal (base 10)?

Solution:
- Use ascii table: http://www.asciitable.com/

Flag:
```
picoCTF{61}
```


## 100 - Bases
Problem:
- What does bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.

Solution:
- Convert Base 64 to ASCII/UTF-8: https://www.base64decode.org/

Flag:
```
picoCTF{l3arn_th3_r0p35}
```


## 100 - First Grep
Problem:
- Can you find the flag in [file](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/first-grep)? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52 on the shell server.

Solution:
```
grep 'picoCTF' first-grep
```

Flag:
```
picoCTF{grep_is_good_to_find_things_4b2451ea}
```


## 100 - Resources
Problem:
- We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag!

Solution:
- Go to: https://picoctf.com/resources
- Scroll to bottom of the page to find the flag.

Flag:
```
picoCTF{r3source_pag3_f1ag} 
```

## 100 - strings it
Problem:
- Can you find the flag in [file](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/strings-it) without running it? You can also find the file in /problems/strings-it_3_8386a6aa560aecfba03c0c6a550b5c51 on the shell server.

Solution
```
strings strings-it | grep 'picoCTF'
```

Flag:
```
picoCTF{5tRIng5_1T_c7fff9e5}
```


## 100 - what's a net cat?
Problem:
- Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 37851 to get the flag?

Solution:
```
nc 2019shell1.picoctf.com 37851
```

Flag:
```
picoCTF{nEtCat_Mast3ry_628e0244}
```


## 200 - Based
Problem:
- To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 20836.

Solution:
- binary -> ascii: https://www.rapidtables.com/convert/number/binary-to-ascii.html
- octal -> ascii: http://www.unit-conversion.info/texttools/octal/
- hex -> ascii: https://www.rapidtables.com/convert/number/hex-to-ascii.html

Flag:
```
picoCTF{learning_about_converting_values_6cdcad0d}
```


## 200 - First  Grep: Part II
Problem:
- Can you find the flag in /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/files on the shell server? Remember to use grep.

Solution:
```
grep -r 'picoCTF' /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/files/
```

Flag:
```
picoCTF{grep_r_to_find_this_5241c61f}
```


## 200 - Plumbing
Problem:
- Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21957.

Solution:
```
nc 2019shell1.picoctf.com 21957 | tee -a plumbing.txt | grep 'picoCTF'
```

Flag:
```
picoCTF{digital_plumb3r_c1082838}
```


## 200 - whats-the-difference
Problem:
- Can you spot the difference? [kitters](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/kitters.jpg) [cattos](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/cattos.jpg). They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server

Solution:
```
cmp -bl cattos.jpg kitters.jpg | awk '{print $3}' | tr -d "\n"
```

Flag:
```
picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
```


## 200 - where-is-the-file
Problem:
- I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e

Solution:
```
ls -a /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e
cat /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e/.cant_see_me
```

Flag:
```
picoCTF{w3ll_that_d1dnt_w0RK_a871629e}
```


## 300 - flag_shop
Problem:
- There's a flag shop selling stuff, can you buy a flag? [Source](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/store.c). Connect with nc 2019shell1.picoctf.com 63894.

Solution:
- Overflow the 4-bit signed integer total_cost to get a negative cost by using a large number, thereby adding to our account balance, giving us enough money to buy the real flag.

Notes:
```
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
2137483600

The final cost is: -410108608

Your current balance after transaction: 410109708

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one1
YOUR FLAG IS: picoCTF{m0n3y_bag5_818a7f84}
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
3
```
Flag:
```
picoCTF{m0n3y_bag5_818a7f84}
```


## 300 - mus1c
Problem:
- I wrote you a [song](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/mus1c_lyrics.txt). Put it in the picoCTF{} flag format

Solution:
- The lyrics are written in Rockstar (https://esolangs.org/wiki/Rockstar, https://github.com/RockstarLang/rockstar). 
- Convert it to decimal using: https://codewithrockstar.com/online. 
- Then convert decimal output to ASCII: https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html

Flag:
```
picoCTF{rrrocknrn0113r}
```


## 350 - 1_wanna_b3_a_r0ck5star
Problem:
- I wrote you another [song](https://github.com/sabinach/ctf/blob/master/2019_picoctf/general_skills/mus1c_lyrics.txt). Put the flag in the picoCTF{} flag format

Solution:
- The lyrics are written in Rockstar again, but this time it's not outputting anything because it's waiting for inputs ("Listen"). 
- Remove the lines: "Listen to.. Music is nothing" and "Else whisper 'That aint it, chief'".
- Convert it to decimal using: https://codewithrockstar.com/online. 
- Then convert decimal output to ASCII: https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html

Flag:
```
picoCTF{BONJOVI} 
```

