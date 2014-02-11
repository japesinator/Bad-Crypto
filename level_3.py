#!/usr/bin/env python
import sys

# Usage: ./level_3.py, then input your plaintext enclosed by quotes

# hint:  github.com/SpiderLabs/cribdrag

secret = input("Please enter your plaintext: ")

def random(size=16):
  return open("/dev/urandom").read(size)

key = random(len(secret))

def strxor(a, b):	 # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

print strxor(secret, key).encode('hex') + "  " + key.encode('hex')
