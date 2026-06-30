"""
08 - AES Encryption and Decryption

Description:
This program implements the Advanced Encryption Standard (AES) algorithm
using ECB, CBC, and CFB modes of operation.

What is AES?
AES (Advanced Encryption Standard) is a symmetric key encryption algorithm
widely used to secure sensitive data. It supports 128-bit, 192-bit, and
256-bit key sizes.

Modes Implemented:

1. ECB (Electronic Codebook)

   * Encrypts each block independently
   * Simple but not recommended for sensitive data

2. CBC (Cipher Block Chaining)

   * Uses an Initialization Vector (IV)
   * Provides better security than ECB

3. CFB (Cipher Feedback)

   * Converts the block cipher into a stream cipher
   * Suitable for encrypting streaming data

Steps Covered:

1. Accept plaintext and encryption key
2. Generate an Initialization Vector (IV)
3. Encrypt data using the selected mode
4. Decrypt ciphertext back to plaintext
5. Display encrypted and decrypted results

Key Concepts:

* AES Algorithm
* Symmetric Key Encryption
* Block Cipher Modes (ECB, CBC, CFB)
* Padding and Unpadding

"""

#pip install pycryptodomex  or   pip install pycryptodome  or pip install cryptodome
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size)

def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size)

def encrypt_cfb(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_cfb(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted

def main():
    plaintext = input("Enter the plaintext: ").encode()
    key = input("Enter the AES key (16, 24, or 32 bytes): ").encode()
    if len(key) not in (16, 24, 32):
      print("Key must be 16, 24, or 32 bytes long.")
      return
    iv = get_random_bytes(AES.block_size)  # Initialization Vector for CBC and CFB

    print("Select encryption mode:")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    mode_choice = int(input("Enter mode choice: "))

    if mode_choice == 1:
        encrypted = encrypt_ecb(plaintext, key)
        decrypted = decrypt_ecb(encrypted, key)
        mode_name = "ECB"
    elif mode_choice == 2:
        encrypted = encrypt_cbc(plaintext, key, iv)
        decrypted = decrypt_cbc(encrypted, key, iv)
        mode_name = "CBC"
    elif mode_choice == 3:
        encrypted = encrypt_cfb(plaintext, key, iv)
        decrypted = decrypt_cfb(encrypted, key, iv)
        mode_name = "CFB"
    else:
        print("Invalid mode choice")
        return

    print("\n" + mode_name + ":")
    print("Plaintext:", plaintext.decode())
    print("Encrypted:", encrypted.hex())
    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    main()
