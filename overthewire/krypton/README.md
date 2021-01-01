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
![lvl2-3.png](https://github.com/sabinach/ctf/blob/master/overthewire/krypton/lvl2-3.png)

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
- Well done. You’ve moved past an easy substitution cipher. 
- The main weakness of a simple substitution cipher is repeated use of a simple key. In the previous exercise you were able to introduce arbitrary plaintext to expose the key. In this example, the cipher mechanism is not available to you, the attacker. However, you have been lucky. You have intercepted more than one message. 
- The password to the next level is found in the file ‘krypton4’. You have also found 3 other files. (found1, found2, found3). 
- You know the following important details: 
	* The message plaintexts are in English (*** very important) 
	* They were produced from the same key (*** even better!). 

Solution:
```
cd /krypton/krypton3
cat krypton4
>>> KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS
```
```
cat HINT1
>>> Some letters are more prevalent in English than others.

cat HINT2
>>> "Frequency Analysis" is your friend.
```
```
cat found1
>>>
CGZNL YJBEN QYDLQ ZQSUQ NZCYD SNQVU BFGBK GQUQZ QSUQN UZCYD SNJDS UDCXJ ZCYDS NZQSU QNUZB WSBNZ QSUQN UDCXJ CUBGS BXJDS UCTYV SUJQG WTBUJ KCWSV LFGBK GSGZN LYJCB GJSZD GCHMS UCJCU QJLYS BXUMA UJCJM JCBGZ CYDSN CGKDC ZDSQZ DVSJJ SNCGJ DSYVQ CGJSO JCUNS YVQZS WALQV SJJSN UBTSX COSWG MTASN BXYBU CJCBG UWBKG JDSQV YDQAS JXBNS OQTYV SKCJD QUDCX JBXQK BMVWA SNSYV QZSWA LWAKB MVWAS ZBTSS QGWUB BGJDS TSJDB WCUGQ TSWQX JSNRM VCMUZ QSUQN KDBMU SWCJJ BZBTT MGCZQ JSKCJ DDCUE SGSNQ VUJDS SGZNL YJCBG UJSYY SNXBN TSWAL QZQSU QNZCY DSNCU BXJSG CGZBN YBNQJ SWQUY QNJBX TBNSZ BTYVS OUZDS TSUUM ZDQUJ DSICE SGNSZ CYDSN QGWUJ CVVDQ UTBWS NGQYY VCZQJ CBGCG JDSNB JULUJ STQUK CJDQV VUCGE VSQVY DQASJ UMAUJ CJMJC BGZCY DSNUJ DSZQS UQNZC YDSNC USQUC VLANB FSGQG WCGYN QZJCZ SBXXS NUSUU SGJCQ VVLGB ZBTTM GCZQJ CBGUS ZMNCJ LUDQF SUYSQ NSYNB WMZSW TBUJB XDCUF GBKGK BNFAS JKSSG QGWDC USQNV LYVQL UKSNS TQCGV LZBTS WCSUQ GWDCU JBNCS UESGN SUDSN QCUSW JBJDS YSQFB XUBYD CUJCZ QJCBG QGWQN JCUJN LALJD SSGWB XJDSU COJSS GJDZS GJMNL GSOJD SKNBJ STQCG VLJNQ ESWCS UMGJC VQABM JCGZV MWCGE DQTVS JFCGE VSQNQ GWTQZ ASJDZ BGUCW SNSWU BTSBX JDSXC GSUJS OQTYV SUCGJ DSSGE VCUDV QGEMQ ESCGD CUVQU JYDQU SDSKN BJSJN QECZB TSWCS UQVUB FGBKG QUNBT QGZSU QGWZB VVQAB NQJSW KCJDB JDSNY VQLKN CEDJU TQGLB XDCUY VQLUK SNSYM AVCUD SWCGS WCJCB GUBXI QNLCG EHMQV CJLQG WQZZM NQZLW MNCGE DCUVC XSJCT SQGWC GJKBB XDCUX BNTSN JDSQJ NCZQV ZBVVS QEMSU YMAVC UDSWJ DSXCN UJXBV CBQZB VVSZJ SWSWC JCBGB XDCUW NQTQJ CZKBN FUJDQ JCGZV MWSWQ VVAMJ JKBBX JDSYV QLUGB KNSZB EGCUS WQUUD QFSUY SQNSU
<<<
```
```
cat found2
>>>
QVJDB MEDGB QJJSG WQGZS NSZBN WUXBN JDSYS NCBWU MNICI STBUJ ACBEN QYDSN UQENS SJDQJ UDQFS UYSQN SKQUS WMZQJ SWQJJ DSFCG EUGSK UZDBB VCGUJ NQJXB NWQXN SSUZD BBVZD QNJSN SWCGQ ABMJQ HMQNJ SNBXQ TCVSX NBTDC UDBTS ENQTT QNUZD BBVUI QNCSW CGHMQ VCJLW MNCGE JDSSV CPQAS JDQGS NQAMJ JDSZM NNCZM VMTKQ UWCZJ QJSWA LVQKJ DNBME DBMJS GEVQG WQGWJ DSUZD BBVKB MVWDQ ISYNB ICWSW QGCGJ SGUCI SSWMZ QJCBG CGVQJ CGENQ TTQNQ GWJDS ZVQUU CZUQJ JDSQE SBXUD QFSUY SQNST QNNCS WJDSL SQNBV WQGGS DQJDQ KQLJD SZBGU CUJBN LZBMN JBXJD SWCBZ SUSBX KBNZS UJSNC UUMSW QTQNN CQESV CZSGZ SBGGB ISTAS NJKBB XDQJD QKQLU GSCED ABMNU YBUJS WABGW UJDSG SOJWQ LQUUM NSJLJ DQJJD SNSKS NSGBC TYSWC TSGJU JBJDS TQNNC QESJD SZBMY VSTQL DQISQ NNQGE SWJDS ZSNST BGLCG UBTSD QUJSU CGZSJ DSKBN ZSUJS NZDQG ZSVVB NQVVB KSWJD STQNN CQESA QGGUJ BASNS QWBGZ SCGUJ SQWBX JDSMU MQVJD NSSJC TSUQG GSUYN SEGQG ZLZBM VWDQI SASSG JDSNS QUBGX BNJDC UUCOT BGJDU QXJSN JDSTQ NNCQE SUDSE QISAC NJDJB QWQME DJSNU MUQGG QKDBK QUAQY JCUSW BGTQL JKCGU UBGDQ TGSJQ GWWQM EDJSN RMWCJ DXBVV BKSWQ VTBUJ JKBLS QNUVQ JSNQG WKSNS AQYJC USWBG XSANM QNLDQ TGSJW CSWBX MGFGB KGZQM USUQJ JDSQE SBXQG WKQUA MNCSW BGQME MUJQX JSNJD SACNJ DBXJD SJKCG UJDSN SQNSX SKDCU JBNCZ QVJNQ ZSUBX UDQFS UYSQN SMGJC VDSCU TSGJC BGSWQ UYQNJ BXJDS VBGWB GJDSQ JNSUZ SGSCG ASZQM USBXJ DCUEQ YUZDB VQNUN SXSNJ BJDSL SQNUA SJKSS GQGWQ UUDQF SUYSQ NSUVB UJLSQ NUACB ENQYD SNUQJ JSTYJ CGEJB QZZBM GJXBN JDCUY SNCBW DQISN SYBNJ SWTQG LQYBZ NLYDQ VUJBN CSUGC ZDBVQ UNBKS UDQFS UYSQN SUXCN UJACB ENQYD SNNSZ BMGJS WQUJN QJXBN WVSES GWJDQ JUDQF SUYSQ NSXVS WJDSJ BKGXB NVBGW BGJBS UZQYS YNBUS ZMJCB GXBNW SSNYB QZDCG EQGBJ DSNSC EDJSS GJDZS GJMNL UJBNL DQUUD QFSUY SQNSU JQNJC GEDCU JDSQJ NCZQV ZQNSS NTCGW CGEJD SDBNU SUBXJ DSQJN SYQJN BGUCG VBGWB GRBDG QMANS LNSYB NJSWJ DQJUD QFSUY SQNSD QWASS GQZBM GJNLU ZDBBV TQUJS NUBTS JKSGJ CSJDZ SGJMN LUZDB VQNUD QISUM EESUJ SWJDQ JUDQF SUYSQ NSTQL DQISA SSGST YVBLS WQUQU ZDBBV TQUJS NALQV SOQGW SNDBE DJBGB XVQGZ QUDCN SQZQJ DBVCZ VQGWB KGSNK DBGQT SWQZS NJQCG KCVVC QTUDQ FSUDQ XJSCG DCUKC VVGBS ICWSG ZSUMA UJQGJ CQJSU UMZDU JBNCS UBJDS NJDQG DSQNU QLZBV VSZJS WQXJS NDCUW SQJD
<<<
```
```
cat found3
>>>
DSNSM YBGVS ENQGW QNBUS KCJDQ ENQIS QGWUJ QJSVL QCNQG WANBM EDJTS JDSAS SJVSX NBTQE VQUUZ QUSCG KDCZD CJKQU SGZVB USWCJ KQUQA SQMJC XMVUZ QNQAQ SMUQG WQJJD QJJCT SMGFG BKGJB GQJMN QVCUJ UBXZB MNUSQ ENSQJ YNCPS CGQUZ CSGJC XCZYB CGJBX ICSKJ DSNSK SNSJK BNBMG WAVQZ FUYBJ UGSQN BGSSO JNSTC JLBXJ DSAQZ FQGWQ VBGEB GSGSQ NJDSB JDSNJ DSUZQ VSUKS NSSOZ SSWCG EVLDQ NWQGW EVBUU LKCJD QVVJD SQYYS QNQGZ SBXAM NGCUD SWEBV WJDSK SCEDJ BXJDS CGUSZ JKQUI SNLNS TQNFQ AVSQG WJQFC GEQVV JDCGE UCGJB ZBGUC WSNQJ CBGCZ BMVWD QNWVL AVQTS RMYCJ SNXBN DCUBY CGCBG NSUYS ZJCGE CJ
<<<
```
```
# frequency analysis with found1, found2, and found3:

# ON PERSONAL MACHINE, RUN:
./frequency_analysis
>>>
# found1
1-gram: S
2-gram: DS
3-gram: JDS
character frequency:
[('S', 155), ('C', 107), ('Q', 106), ('J', 102), ('U', 100), ('B', 87), ('G', 81), ('N', 74), ('D', 69), ('Z', 57), ('V', 56), ('W', 47), ('Y', 42), ('T', 32), ('M', 29), ('X', 29), ('L', 27), ('K', 25), ('A', 20), ('E', 17), ('F', 11), ('O', 7), ('I', 2), ('H', 2), ('R', 1)]
----------------
# found2
1-gram: S
2-gram: JD
3-gram: JDS
character frequency:
[('S', 243), ('Q', 186), ('J', 158), ('N', 135), ('U', 130), ('B', 129), ('D', 119), ('G', 111), ('C', 86), ('W', 66), ('Z', 59), ('V', 53), ('M', 45), ('T', 37), ('E', 34), ('Y', 33), ('X', 33), ('K', 30), ('L', 27), ('A', 26), ('I', 14), ('F', 12), ('O', 3), ('H', 2), ('R', 2), ('P', 1)]
----------------
# found3
1-gram: S
2-gram: JD
3-gram: JDS
character frequency:
[('S', 58), ('Q', 48), ('J', 41), ('G', 35), ('C', 34), ('N', 31), ('B', 30), ('U', 27), ('D', 22), ('V', 21), ('W', 16), ('Z', 16), ('E', 13), ('K', 12), ('M', 12), ('A', 9), ('Y', 9), ('X', 9), ('L', 6), ('T', 6), ('F', 5), ('I', 3), ('O', 2), ('P', 1), ('R', 1)]
<<<
```
```
# NOTES:
# replace J --> t, D --> h, S --> e
# Q is the 2nd most common letter, so Q --> a

# OTHER NOTES:
# 


# ON PERSONAL MACHINE, RUN:
./caesar_cipher_manual.py "KSVVW BGSJD SVSIS VXBMN YQUUK BNWCU ANMJS"
```

Helpful Links:
* https://en.wikipedia.org/wiki/Frequency_analysis

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
