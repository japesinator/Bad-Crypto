#!/usr/bin/env python
from time import sleep

# Usage: ./bonus_level.py, then input your plaintext enclosed by quotes

# Note:  I haven't made a ciphertext for this because the attack on it depends
# a lot on the machine it was implemented on

secret = input("Please enter your plaintext: ")

def random(size=16):
  return open("/dev/urandom").read(size)

key = random(len(secret))

def strxor(a, b):	 # xor two strings of different lengths
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

log_counter = 0xFF

for char in secret:
  for i in range(ord(char)):
    sleep(0.01)
    log_counter ^= i
  print log_counter

print strxor(secret, key).encode('hex')
