"""
03 - Hill Cipher (2x2 Matrix)

Description:
This program implements the Hill Cipher using a 2x2 key matrix for both
encryption and decryption.

What is Hill Cipher?
Hill Cipher is a classical encryption technique based on linear algebra.
It uses matrix multiplication to encrypt blocks of plaintext.

Why It is Important?

* Introduces matrix-based encryption
* Stronger than simple substitution ciphers
* Foundation for modern cryptographic techniques

Steps Covered:

1. Convert plaintext into numerical values (A=0 to Z=25)
2. Divide plaintext into pairs of characters
3. Apply matrix multiplication with key matrix
4. Perform modulo 26 operation
5. Generate ciphertext
6. Compute inverse key matrix for decryption
7. Recover original plaintext

Key Concepts:

* Modular arithmetic
* Matrix multiplication
* Modular inverse

"""

import numpy as np

# Function to find modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None  # If inverse doesn't exist

# Function to encrypt using 2x2 Hill cipher
def hill_cipher_2x2_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding

    # Key matrix must be invertible modulo 26 for decryption to work
    key_matrix = np.array(key).reshape(2, 2)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        pair = np.array([[ord(plaintext[i]) - 65], [ord(plaintext[i+1]) - 65]])
        result = np.dot(key_matrix, pair) % 26
        ciphertext += chr(result[0][0] + 65) + chr(result[1][0] + 65)

    return ciphertext

# Function to decrypt using 2x2 Hill cipher
def hill_cipher_2x2_decrypt(ciphertext, key, size):
    key_matrix = np.array(key).reshape(2, 2)
    a, b = key_matrix[0]
    c, d = key_matrix[1]
    det = int((a * d - b * c) % 26)

    inv_det = mod_inverse(det, 26)
    if inv_det is None:
        raise ValueError("Key matrix is not invertible modulo 26.")

    # Compute adjugate matrix and multiply by modular inverse of determinant
    adj = np.array([[d, -b], [-c, a]]) % 26
    inv_key = (inv_det * adj) % 26

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        pair = np.array([[ord(ciphertext[i]) - 65], [ord(ciphertext[i+1]) - 65]])
        result = np.dot(inv_key, pair) % 26
        plaintext += chr(int(result[0][0]) + 65) + chr(int(result[1][0]) + 65)

    if size % 2 != 0:
        plaintext = plaintext[:size]  # Remove padding

    return plaintext

# Example usage
plaintext = "HELLO"
size = len(plaintext)
key = [[3, 4], [2, 3]]

ciphertext = hill_cipher_2x2_encrypt(plaintext, key)
decrypted_plaintext = hill_cipher_2x2_decrypt(ciphertext, key, size)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
