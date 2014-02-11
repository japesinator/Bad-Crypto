#! /usr/bin/env python

# Usage: ,/level_1.py, then input your plaintext enclosed by quotes

# Hint: this is a chain of easy-to-reverse functions

secret = input("Please enter your plaintext: ")

print secret.encode('hex')[1:] + secret.encode('hex')[::-1][-1]
