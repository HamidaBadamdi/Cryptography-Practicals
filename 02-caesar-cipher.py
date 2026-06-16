"""
02 - Caesar Cipher Implementation

Description:
This program implements the Caesar Cipher, a classical encryption technique
that shifts each letter in a message by a fixed number of positions.

What is Caesar Cipher?
It is a substitution cipher where each character in the plaintext is replaced
by another character a fixed number of positions down the alphabet.

Why It is Important?

* One of the simplest encryption techniques
* Helps understand basic cryptographic concepts
* Foundation for more advanced algorithms

Steps Covered:

1. Define input message and shift value
2. Apply shifting logic for uppercase and lowercase letters
3. Preserve non-alphabet characters
4. Generate encrypted message

"""

def caesar_cipher(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isupper():
            encrypted_char = chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted_char = chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_message += encrypted_char

    return encrypted_message
def decrypt_caesar(cipher, shift):
    return caesar_cipher(cipher, -shift)

message = "Hello, world!"
shift = 3
encrypted_message = caesar_cipher(message, shift)

print("Original message:", message)
print("Shift:", shift)
print("Encrypted message:", encrypted_message)
