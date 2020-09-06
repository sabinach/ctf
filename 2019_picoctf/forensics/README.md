# Forensics

## XXX
Problem:
- XXX

Solution:
- XXX

Flag:
```
XXX
```


## Glory of the Garden (50 points)
Problem:
- This [garden](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/garden.jpg) contains more than it seems. You can also find the file in /problems/glory-of-the-garden_4_cf9f4aaf458caf5268f8cf0a6465eb98 on the shell server.

Solution:
- Use hex editor and search for the string "picoCTF"

Flag:
```
picoCTF{more_than_m33ts_the_3y36BCA684D}
```


## unzip (50 points)
Problem:
- Can you unzip this [file](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/unzip-flag.zip) and get the flag?

Solution:
```
unzip unzip-flag.zip
```

Flag:
```
picoCTF{unz1pp1ng_1s_3a5y}
```


## So Meta (150 points)
Problem:
- Find the [flag](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/pico_img.png) in this picture. You can also find the file in /problems/so-meta_0_7c0b2ae7a38b024c6b1c68cf50970a88.

Solution:
- Use hex editor and search for the string "picoCTF"

Flag:
```
picoCTF{s0_m3ta_dc38ce45}
```


## What Lies Within (150 points)
Problem:
- Theres something in the [building](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/buildings.png). Can you retrieve the flag?

Solution:
- Go to https://stylesuxx.github.io/steganography/
- Decode ```buildings.png```

Flag:
```
picoCTF{h1d1ng_1n_th3_b1t5}
```


## extensions (150 points)
Problem:
- This is a really weird text file [TXT](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/extensions.txt)? Can you find the flag?

Solution:
- Go to https://convertio.co/txt-png/
- Upload ```extensions.txt```, and the website will convert to ```extensions.png``` that will contain an image of the flag

Flag:
```
picoCTF{now_you_know_about_extensions}
```


## shark on wire 1 (150 points)
Problem:
- We found this [packet capture](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/capture.pcap). Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.

Solution:
- Open [WireShark](https://www.wireshark.org/)
- Upload the given ```capture.pcap``` file on WireShark
- Note that individual UDP packets are broken up or malformed
- Right-click a random ```UDP packet --> Follow --> UDP Stream``` (you might have to do this a few times before you follow the correct stream)

Flag:
```
picoCTF{StaT31355_636f6e6e}
```


## WhitePages (250 points)
Problem:
- I stopped using YellowPages and moved onto WhitePages... but the [page they gave me](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/whitepages.txt) is all blank!

Solution:
- Open the file using a text editor with a black background, and notice that the file consists of only SPACES and DOTS
- Notice that it looks like morse code, but it's not
- Open a hex editor to view the hex values of the original file
- Notice that comparing the original file and its corresponding hex values, SPACES correspond to ```20``` in hex, and DOTS correspond to ```E28083``` in hex
- Replace ```20``` --> ```1``` (aka spaces), and ```E28083``` --> ```0``` (aka dots)
- Convert this new binary representation to ASCII: https://www.rapidtables.com/convert/number/binary-to-ascii.html

Image of the original SPACES and DOTS
![WhitePages Spaces and Dots](https://github.com/sabinach/ctf/blob/master/2019_picoctf/forensics/whitepages.png)

Original Hex
```
E28083E2 8083E280 83E28083 20E28083 20E28083 E28083E2 8083E280 83E28083 20E28083 E2808320 E28083E2 8083E280 83E28083 20E28083 E2808320 E2808320 2020E280 83E28083 E28083E2 8083E280 832020E2 808320E2 8083E280 8320E280 832020E2 8083E280 83E28083 2020E280 832020E2 80832020 2020E280 8320E280 83E28083 E28083E2 80832020 E2808320 E2808320 E2808320 E28083E2 8083E280 8320E280 83E28083 E2808320 20E28083 E28083E2 8083E280 83E28083 20E28083 20E28083 E28083E2 8083E280 83E28083 20E28083 20E28083 E28083E2 8083E280 83E28083 20E28083 E2808320 E28083E2 8083E280 83E28083 20E28083 E2808320 E2808320 E2808320 E28083E2 80832020 E2808320 E28083E2 8083E280 8320E280 8320E280 8320E280 83E28083 E2808320 E2808320 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 8320E280 83E28083 E28083E2 8083E280 8320E280 8320E280 8320E280 8320E280 8320E280 83E28083 E28083E2 808320E2 8083E280 8320E280 83E28083 2020E280 83E28083 E2808320 E28083E2 808320E2 8083E280 8320E280 8320E280 83E28083 E28083E2 80832020 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 8320E280 83E28083 20E28083 E2808320 E28083E2 8083E280 8320E280 8320E280 8320E280 83E28083 E28083E2 80832020 E2808320 E28083E2 80832020 2020E280 8320E280 8320E280 83E28083 20E28083 E2808320 E28083E2 8083E280 8320E280 83E28083 E2808320 E2808320 E28083E2 80832020 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 83E28083 20E28083 E2808320 20E28083 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 83E28083 E28083E2 808320E2 8083E280 8320E280 83E28083 E28083E2 8083E280 8320E280 8320E280 83E28083 E28083E2 80832020 E2808320 E28083E2 808320E2 80832020 E2808320 E28083E2 8083E280 83202020 E2808320 E2808320 E28083E2 808320E2 8083E280 8320E280 83E28083 20202020 E2808320 E2808320 E2808320 E2808320 E2808320 E28083E2 80832020 20E28083 E2808320 E28083E2 8083E280 8320E280 83E28083 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 8320E280 83E28083 20E28083 E2808320 E28083E2 8083E280 8320E280 8320E280 8320E280 8320E280 83E28083 E28083E2 8083E280 8320E280 83E28083 20202020 E2808320 E2808320 E28083E2 808320E2 8083E280 8320E280 8320E280 8320E280 83E28083 E28083E2 8083E280 83E28083 20E28083 20E28083 E28083E2 8083E280 83E28083 20E28083 E2808320 E28083E2 8083E280 83E28083 20E28083 E2808320 E28083E2 80832020 E2808320 E2808320 E28083E2 80832020 E28083E2 8083E280 83E28083 E28083E2 80832020 E28083E2 8083E280 83E28083 E28083E2 80832020 E28083E2 8083E280 83E28083 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 83E28083 E2808320 20E28083 E2808320 20E28083 20202020 E2808320 2020E280 83E28083 20E28083 E2808320 20E28083 E28083E2 808320E2 8083E280 832020E2 8083E280 8320E280 8320E280 83202020 E28083E2 80832020 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 83E28083 E28083E2 8083E280 8320E280 83202020 E2808320 20E28083 E2808320 20E28083 E2808320 E2808320 E28083E2 808320E2 80832020 E28083E2 8083E280 83E28083 20E28083 E28083E2 8083E280 83E28083 E2808320 E2808320 E28083E2 8083E280 83E28083 E2808320 20E28083 20E28083 E2808320 E2808320 2020E280 8320E280 83E28083 E2808320 2020E280 8320E280 83E28083 E2808320 2020E280 83E28083 2020E280 832020E2 8083E280 83E28083 20E28083 E2808320 2020E280 8320E280 8320E280 83202020 E28083E2 808320E2 8083E280 832020E2 8083E280 83202020 E2808320 20E28083 20E28083 E28083E2 8083E280 83E28083 20E28083 2020E280 83E28083 E28083E2 808320E2 8083E280 83E28083 E28083E2 8083E280 8320E280 8320E280 83E28083 E28083E2 8083E280 8320E280 83E28083 E28083E2 8083E280 8320E280 83E28083 20E28083 E28083E2 8083E280 83E28083 E28083E2 80832020 E28083E2 8083E280 8320E280 83E28083 2020E280 8320E280 8320E280 83E28083 2020E280 83E28083 20E28083 E28083E2 80832020 E28083E2 8083E280 8320E280 83E28083 2020E280 83E28083 2020E280 83E28083 E28083E2 808320E2 808320E2 8083E280 83E28083 E28083E2 808320E2 8083E280 8320E280 83E28083 E28083E2 808320E2 8083E280 8320E280 83202020 E28083E2 8083E280 83E28083 E2808320 20E28083 20E28083 E2808320 E2808320 20E28083 E28083E2 80832020 E2808320 20E28083 20202020 E2808320 E28083E2 8083E280 83E28083 2020E280 8320E280 8320E280 8320E280 83E28083 E2808320 E28083E2 8083E280 832020E2 8083E280 83202020 20E28083 2020E280 832020E2 80832020 20E28083 E2808320 20E28083 20202020 E2808320 2020E280 8320E280 83E28083 E2808320 E2808320 20202020 E2808320 20E28083 E28083E2 8083E280 8320E280 832020E2 80832020 E28083E2 8083E280 832020E2 80832020 E28083E2 8083E280 8320E280 83202020 2020E280 83202020 E28083E2 80832020 E2808320 2020E280 83E28083 E28083E2 8083E280 832020E2 8083E280 83E28083 E2808320 E2808320 20E28083 E28083E2 80832020 E2808320 20E28083 E2808320 E2808320 E2808320 2020E280 83E28083 2020E280 8320E280 83202020 2020E280 832020E2 8083E280 83E28083 E2808320 E2808320 2020E280 83E28083 20E28083 E2808320 20E28083 E2808320 E2808320 E2808320 E2808320 20202020 E2808320 20E28083 E28083E2 80832020 E2808320 2020E280 83E28083 20E28083 E2808320 20E28083 E2808320 E2808320 E2808320 20E28083 E28083E2 8083E280 8320E280 83202020 E2808320 E28083E2 8083E280 832020E2 8083E280 8320E280 8320E280 832020E2 8083E280 8320E280 83E28083 E2808320 E2808320 20202020 E2808320 20E28083 E2808320 E2808320 E2808320 2020E280 83E28083 E2808320 E2808320 2020E280 8320E280 8320E280 832020E2 8083E280 83E28083 E2808320 E2808320 20E28083 2020E280 83E28083 E2808320 E2808320 20202020 E2808320 20E28083 E2808320 E28083E2 8083E280 832020E2 8083E280 8320E280 83E28083 E28083E2 80832020 E2808320 E2808320 E2808320 20E28083 E28083E2 80832020 E28083E2 80832020 E28083E2 808320E2 8083E280 832020E2 8083E280 8320E280 8320E280 83E28083 2020E280 83E28083 20E28083 E2808320 20E28083 E2808320 20E28083 E28083E2 80832020 E2808320 2020E280 83E28083 2020E280 83202020 E2808320 20E28083 E2808320 20E28083 E28083E2 80832020 20E28083 E28083E2 8083E280 83E28083 202020E2 8083E280 8320E280 832020E2 8083E280 832020E2 8083E280 83E28083 2020E280 83E28083 2020E280 83E28083 2020E280 83E28083 E28083E2 8083E280 83E28083 2020E280 8320E280 8320E280 83E28083 2020E280 83E28083 E2808320 E2808320 20E28083 E28083E2 80832020 E28083E2 80832020 20E28083 E28083E2 8083E280 83E28083 2020E280 83E28083 20E28083 E2808320 20E28083 E28083E2 808320E2 8083E280 832020E2 8083E280 832020E2 8083E280 832020E2 8083E280 8320E280 8320E280 832020E2 8083E280 8320E280 8320E280 83E28083 2020E280 83202020 E2808320 20E28083 E2808320 E28083E2 8083E280 83E28083 202020E2 8083E280 8320E280 83E28083 202020E2 8083E280 8320E280 83E28083 2020E280 832020E2 8083E280 832020E2 8083E280 8320E280 8320E280 832020E2 8083E280 832020E2 8083E280 83202020 2020E280 8320E280 83E28083 E28083E2 808320E2 808320E2 8083E280 83E28083 E28083E2 808320E2 8083E280 8320E280 83E28083 E28083E2 808320E2 8083E280 8320
```

Converted Binary
```
00001010000010010000100101110000011010010110001101101111010000110101010001000110000010100000101000001001000010010101001101000101010001010010000001010000010101010100001001001100010010010100001100100000010100100100010101000011010011110101001001000100010100110010000000100110001000000100001001000001010000110100101101000111010100100100111101010101010011100100010000100000010100100100010101010000010011110101001001010100000010100000100100001001001101010011000000110000001100000010000001000110011011110111001001100010011001010111001100100000010000010111011001100101001011000010000001010000011010010111010001110100011100110110001001110101011100100110011101101000001011000010000001010000010000010010000000110001001101010011001000110001001100110000101000001001000010010111000001101001011000110110111101000011010101000100011001111011011011100110111101110100010111110110000101101100011011000101111101110011011100000110000101100011011001010111001101011111011000010111001001100101010111110110001101110010011001010110000101110100011001010110010001011111011001010111000101110101011000010110110001011111011001000110010000110101011000110011001001100101001100100110011000110111001101110110011000111000001110010110011000110011001100000011010100110001011000110011100000110010011000100110011001100101011001010011011101100100001110010011100100110110011001010110011001111101000010100000100100001001
```

Flag:
```
picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}
```

