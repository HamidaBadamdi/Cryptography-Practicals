"""
01 - XOR Operation on String

Description:
This program demonstrates a basic cryptographic operation using XOR on each
character of a string.

What is XOR?
XOR (Exclusive OR) is a fundamental operation used in cryptography.
It compares two bits and returns:

* 1 if bits are different
* 0 if bits are same

Why XOR in Cryptography?
XOR is widely used in encryption algorithms because:

* It is simple and fast
* It can be reversed using the same operation

Steps Covered:

1. Define a string
2. Apply XOR operation on each character
3. Convert result back to characters
4. Display transformed output

Note:
XOR with 0 returns the same value, while XOR with 1 slightly modifies the character.

"""
string = "abcd"
result = ""

for char in string:
    # XOR the character with 1
    xor_char = chr(ord(char) ^ 1)
    result += xor_char
print(result)
