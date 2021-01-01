#!/usr/bin/env python

import sys

def decrypt(text, shift): 
  result = "" 

  for i in range(len(text)): 
    char = text[i]
    if char == " ":
      result += " " 
    elif (char.isupper()): 
        result += chr((ord(char) + shift - 65) % 26 + 65) 
    else:
      result += chr((ord(char) + shift - 97) % 26 + 97) 

  return result 

def main():
  if len(sys.argv) == 2:
    text = sys.argv[1]
    print("Text: " + text)

    for shift in range(27):
      print("---")
      print("Shift: " + str(shift))
      print("Decrypted: " + decrypt(text, shift))

  else:
    print("To run: ./caesar_cipher.py string-to-decrypt")

main()