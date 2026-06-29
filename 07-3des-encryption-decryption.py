"""
07 - Triple DES (3DES) Encryption and Decryption

Description:
This program implements the Triple Data Encryption Standard (3DES) algorithm
using three different modes of operation: ECB, CBC, and CFB.

What is 3DES?
Triple DES (3DES) is a symmetric key encryption algorithm that applies the
DES cipher three times to each data block, providing stronger security than
the original DES algorithm.

Modes Implemented:
1. ECB (Electronic Codebook)
   - Encrypts each block independently
   - Simple but less secure

2. CBC (Cipher Block Chaining)
   - Uses an Initialization Vector (IV)
   - Each ciphertext block depends on the previous block

3. CFB (Cipher Feedback)
   - Converts the block cipher into a stream cipher
   - Suitable for encrypting data streams

Steps Covered:
1. Accept plaintext and encryption key
2. Generate an Initialization Vector (IV)
3. Encrypt data using the selected mode
4. Decrypt ciphertext back to plaintext
5. Display encryption and decryption results

Key Concepts:
- Triple DES (3DES)
- Symmetric Key Cryptography
- Block Cipher Modes (ECB, CBC, CFB)
- Padding and Unpadding

"""
#pip install pycryptodomex  or   pip install pycryptodome  or pip install cryptodome
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_ecb(plaintext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, 8))
    return ciphertext

def decrypt_ecb(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, 8)

def encrypt_cbc(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, 8))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, 8)

def encrypt_cfb(plaintext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt_cfb(ciphertext, key, iv):
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted

def main():
    plaintext = input("Enter the plaintext: ").encode()
    key = input("Enter the 3DES key (16 or 24 bytes): ").encode()
   
    if len(key) not in (16, 24):
       print("Key must be either 16 or 24 bytes long.")
       return
    iv = get_random_bytes(8)  # Initialization Vector for CBC and CFB

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
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted.decode())

if __name__ == "__main__":
    main()
