#!/usr/bin/env python

import sys

ORIGINAL = "abcdefghijklmnopqrstuvwxyz"
SHIFT = "abcdefghijklmnopqrstuvwxyz"

def decrypt(original, shift, text): 
  result = "" 

  for i in range(len(text)): 
    char = text[i]
    if char == " ":
      result += " " 
    elif (char.isupper()): 
      index = original.index(char.lower())
      result += shift[index].upper()
    else:
      index = original.index(char)
      result += shift[index]

  return result 

def main():
  if len(sys.argv) == 2:
    text = sys.argv[1]
    print("Text: " + text)
    print("---")
    print("Original -> Shift: " + ORIGINAL + " -> " + SHIFT)
    print("Decrypted: " + decrypt(ORIGINAL, SHIFT, text))

  else:
    print("To run: ./caesar_cipher.py string-to-decrypt")

main()