"""
12 - MD5 Hashing

Description:
This program demonstrates the MD5 hashing algorithm by generating
the hash value of user-input text and displaying the hash bytes
along with the output size.

Key Concepts:
- MD5 Hashing
- Message Digest
- Hash Output Size

"""
import hashlib
import sys

str= input("enter the value  ")

str=bytes(str,'utf-8')
result= hashlib.md5(str);
print("the byte equivalent of hash is :", end="")
print(result.digest())

print("\r")
print("the size of output :",end="")
print(sys.getsizeof(result.digest()))

str= input("enter the value  ")

str=bytes(str,'utf-8')
result= hashlib.md5(str);
print("the byte equivalent of hash is :", end="")
print(result.digest())

print("\r")
print("the size of output :",end="")
print(sys.getsizeof(result.digest()))
