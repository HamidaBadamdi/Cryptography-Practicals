"""
05 - Rail Fence Cipher Implementation

Description:
This program implements the Rail Fence Cipher, a classical transposition
cipher that rearranges characters in a zigzag pattern.

What is Rail Fence Cipher?
It is a transposition cipher where plaintext is written in a zigzag pattern
across multiple rows (rails) and then read row by row to form ciphertext.

Why It is Important?

* Demonstrates transposition-based encryption
* Easy to understand and implement
* Introduces pattern-based encryption techniques

Steps Covered:

1. Define plaintext and number of rails
2. Traverse text in zigzag manner
3. Store characters in rails
4. Concatenate rows to form ciphertext

Key Concepts:

* Zigzag traversal
* Transposition cipher
* Pattern-based encryption

"""

def rail_fence_cipher(plaintext, rails):
    fence = [[] for i in range(rails)]
    rail = 0
    direction = 1
    for letter in plaintext:
        fence[rail].append(letter)
        rail += direction
        if rail == rails-1 or rail == 0:
            direction = -direction
    
    ciphertext = ""
    for rail in fence:
        for letter in rail:
            ciphertext += letter
    
    return ciphertext

plaintext = "HELLO WORLD"
rails = 3
ciphertext = rail_fence_cipher(plaintext, rails)

print("Plaintext:", plaintext)
print("Rails:", rails)
print("Ciphertext:", ciphertext)
