#!/usr/bin/env python
from time import sleep

# Usage: ./bonus_level.py, then input your plaintext enclosed by quotes

# Note:  I haven't made a ciphertext for this because the attack on it depends
# a lot on the machine it was implemented on

secret = input("Please enter your plaintext: ")

for char in secret:
  for i in range(ord(char)):
    sleep(0.01)
    log_counter ^= i
  print log_counter
