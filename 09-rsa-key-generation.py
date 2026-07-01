"""
09 - RSA Key Pair Generation

Description:
This program generates an RSA public and private key pair using the
Python cryptography library and stores them as PEM files.

What is RSA?
RSA is an asymmetric encryption algorithm that uses two different keys:

* Public Key: Used for encryption
* Private Key: Used for decryption

Why Key Generation?
Before encrypting or decrypting data using RSA, a secure public-private
key pair must be generated.

Steps Covered:

1. Generate a 2048-bit RSA private key
2. Derive the corresponding public key
3. Save the private key in PEM format
4. Save the public key in PEM format

Key Concepts:

* Asymmetric Cryptography
* Public Key
* Private Key
* PEM File Format

"""


from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_keys():
    # Generate private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    # Save private key
    with open("receiver_private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Generate and save public key
    public_key = private_key.public_key()
    with open("receiver_public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    print("✅ RSA Key pair generated successfully.")

if __name__ == "__main__":
    generate_keys()
