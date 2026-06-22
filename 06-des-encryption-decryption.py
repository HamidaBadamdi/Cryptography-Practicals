"""
06 - DES Encryption and Decryption

Description:
This program implements Data Encryption Standard (DES) algorithm using
different modes of operation: ECB, CBC, and CFB.

What is DES?
DES is a symmetric key block cipher that encrypts data in 64-bit blocks
using a 56-bit key (represented as 8 bytes).

Modes Implemented:

1. ECB (Electronic Codebook)

   * Simplest mode
   * Encrypts each block independently

2. CBC (Cipher Block Chaining)

   * Uses Initialization Vector (IV)
   * Each block depends on previous block

3. CFB (Cipher Feedback)

   * Converts block cipher into stream cipher
   * Suitable for real-time encryption

Steps Covered:

1. Take user input (plaintext, key, mode)
2. Apply encryption based on selected mode
3. Decrypt ciphertext back to original text
4. Display encrypted and decrypted output

Key Concepts:

* Symmetric encryption
* Block cipher modes
* Padding and unpadding

"""


#pip install pycryptodomex  or   pip install pycryptodome  or pip install cryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_ecb(data, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, 8))
    return ciphertext

def decrypt_ecb(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), 8)
    return plaintext

def encrypt_cbc(data, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data, 8))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), 8)
    return plaintext

def encrypt_cfb(data, key, iv):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def decrypt_cfb(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CFB, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    mode = input("Select mode (ECB, CBC, CFB): ").upper()
    data = input("Enter plain text: ").encode()
    key = input("Enter key (8 bytes): ").encode()
    #iv = get_random_bytes(8)  # Initialization vector for CBC and CFB modes
    iv = input("Enter initialization vector for CBC and CFB modes (8 bytes): ").encode()

    if len(key) != 8:
        print("Key must be 8 bytes long.")
        return

    if mode == "ECB":
        ciphertext = encrypt_ecb(data, key)
        decrypted_text = decrypt_ecb(ciphertext, key)
    elif mode == "CBC":
        ciphertext = encrypt_cbc(data, key, iv)
        decrypted_text = decrypt_cbc(ciphertext, key, iv)
    elif mode == "CFB":
        ciphertext = encrypt_cfb(data, key, iv)
        decrypted_text = decrypt_cfb(ciphertext, key, iv)
    else:
        print("Invalid mode selected.")
        return

    print("Ciphertext:", ciphertext.hex())
    print("Decrypted text:", decrypted_text.decode())

if __name__ == "__main__":
    main()
