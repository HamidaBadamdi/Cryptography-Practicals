"""
12 - SHA-1 and SHA-512 Hashing

Description:
This program demonstrates SHA-1 and SHA-512 hashing algorithms by
generating hash values for a given input string using Python's hashlib library.

Key Concepts:
- SHA-1 Hashing
- SHA-512 Hashing
- Cryptographic Hash Functions

"""
import hashlib

str="abhaydodiya"

result=hashlib.sha512(str.encode())

print(result.hexdigest())
print("\r")
result=hashlib.sha1(str.encode())

print(result.hexdigest())
