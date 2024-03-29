# Reverse Engineering

## Notes:
To run code in java (Mac):
- ```javac <filename>.java```
- This will compile the file, and generate a Java byte code named <filename>.class
- ```java <filename>```


## XXX
Problem:
- XXX

Solution:
- XXX

Flag:
```
picoCTF{XXX}
```


## 50 - vault-door-training
Problem:
- Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility. The source code for the training vault is here: [VaultDoorTraining.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoorTraining.java)

Solution:
- VaultDoorTraining.java hardcodes the flag in its code line 24 (big yikes)

Flag:
```
picoCTF{w4rm1ng_Up_w1tH_jAv4_ca5ae7fcc95}
```


## 100 - vault-door-1
Problem:
- This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: [VaultDoor1.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoor1.java)

Solution:
- VaultDoor1.java also hardcodes the flag in its code, but we need to unscramble it based on character position (better, but still yikes)

Flag:
```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_63ef3a}
```


## 200 - vault-door-3
Problem:
- This vault uses for-loops and byte arrays. The source code for this vault is here: [VaultDoor3.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoor3.java)

Solution:
- I hardcoded the string in line 42 as the `password` variable so that the code applies the changes to the final string, and then printed out the final string buffer.

Flag:
```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c79a21}
```


## 250 - vault-door-4
Problem:
- This vault uses ASCII encoding for the password. The source code for this vault is here: [VaultDoor4.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoor4.java)

Solution:
- Looked up an ASCII table and looked up each char depending on if the bytes were dec, hex, oct, or char. Very tedious..

Flag:
```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_f4a8cd8f7e}
```


## 300 - vault-door-5
Problem:
- In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: [VaultDoor5.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoor5.java)

Solution:
1. Decode Base64 -> ASCII: https://www.base64decode.org/
2. Decode ASCII -> UTF-8: https://www.urldecoder.org/

Flag:
```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_84fd5095}
```


## 350 - vault-door-6
Problem:
- This vault uses an XOR encryption scheme. The source code for this vault is here: [VaultDoor6.java](https://github.com/sabinach/ctf/blob/master/2019_picoctf/reverse_engineering/VaultDoor6.java)

Solution:
- XXX

Flag:
```
picoCTF{XXX}
```
