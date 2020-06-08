# General Skills

## 50 - 2Warm
Can you convert number 42 (base 10) 
```
picoCTF{101010}
```

## 50 - Lets Warm Up
If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?
```
picoCTF{p}
``` 

## 50 - Warmed Up
What is 0x3D (base 16) in decimal (base 10)?
```
picoCTF{61}
```

## 100 - Bases
What does bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.
```
Solution: Base 64 to ASCII/UTF-8
picoCTF{l3arn_th3_r0p35}
```

## 100 - First Grep
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_0_93be1631acf1a93b98cdcc3e7b9fdc52 on the shell server.
```
grep 'picoCTF' first-grep
picoCTF{grep_is_good_to_find_things_4b2451ea}
```

## 100 - Resources
We put together a bunch of resources to help you out on our website! If you go over there, you might even find a flag! https://picoctf.com/resources
```
picoCTF{r3source_pag3_f1ag} 
```

## 100 - strings it
Can you find the flag in file without running it? You can also find the file in /problems/strings-it_3_8386a6aa560aecfba03c0c6a550b5c51 on the shell server.
```
strings strings-it | grep 'picoCTF'
picoCTF{5tRIng5_1T_c7fff9e5}
```

## 100 - what's a net cat?
Using netcat (nc) is going to be pretty important. Can you connect to 2019shell1.picoctf.com at port 37851 to get the flag?
```
nc 2019shell1.picoctf.com 37851
picoCTF{nEtCat_Mast3ry_628e0244}
```

## 200 - Based
To get truly 1337, you must understand different data encodings, such as hexadecimal or binary. Can you get the flag from this program to prove you are on the way to becoming 1337? Connect with nc 2019shell1.picoctf.com 20836.
```
binary -> ascii, octal -> ascii, hex -> ascii
picoCTF{learning_about_converting_values_6cdcad0d}
```

## 200 - First  Grep: Part II
Can you find the flag in /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/files on the shell server? Remember to use grep.
```
grep -r 'picoCTF' /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/files/
picoCTF{grep_r_to_find_this_5241c61f}
```

## 200 - Plumbing
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to 2019shell1.picoctf.com 21957.
```
nc 2019shell1.picoctf.com 21957 | tee -a plumbing.txt | grep 'picoCTF'
picoCTF{digital_plumb3r_c1082838}
```

## 200 - whats-the-difference
Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server
```
cmp -bl cattos.jpg kitters.jpg | awk '{print $3}' | tr -d "\n"
picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}
```

## 200 - where-is-the-file
I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e
```
ls -a /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e
cat /problems/where-is-the-file_5_5302300652950d2248ac8bb0042d115e/.cant_see_me
picoCTF{w3ll_that_d1dnt_w0RK_a871629e}
```

## 300 - flag_shop
There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 63894.
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
```
Overflow the 4-bit signed integer total_cost to get a negative cost, thereby adding to our account balance, giving us enough money to buy the real flag.
picoCTF{m0n3y_bag5_818a7f84}
```

## 300 - mus1c
I wrote you a song. Put it in the picoCTF{} flag format
```
The lyrics are written in Rockstar (https://esolangs.org/wiki/Rockstar, https://github.com/RockstarLang/rockstar). Convert it to decimal using: https://codewithrockstar.com/online. Then convert decimal output to ASCII.
picoCTF{rrrocknrn0113r}
```

## 350 - 1_wanna_b3_a_r0ck5star
I wrote you another song. Put the flag in the picoCTF{} flag format
 ```
The lyrics are written in Rockstar again, but this time it's not outputting anything because it's waiting for inputs ("Listen"). Remove the lines: "Listen to.. Music is nothing" and "Else whisper 'That aint it, chief'", and convert the rest of the lyrics to decimal -> ASCII.
picoCTF{BONJOVI} 
```

