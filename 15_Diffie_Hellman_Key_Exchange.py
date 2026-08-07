"""
Practical 15: Diffie-Hellman Key Exchange Algorithm

Objective:
To implement the Diffie-Hellman Key Exchange algorithm for securely generating
a shared secret key between two communicating parties over an insecure channel.

Tools Used:
- Python

Procedure:
1. Choose a prime number and a primitive root.
2. Generate public keys using private keys.
3. Exchange public keys between both parties.
4. Compute the shared secret key independently.
5. Verify that both parties obtain the same secret key.

Outcome:
Successfully implemented the Diffie-Hellman Key Exchange algorithm and generated
a common shared secret key for secure communication.

"""

# Diffie-Hellman Key Exchange Algorithm

# Function to calculate (base^exp) % mod
def power(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

# Function to perform Diffie-Hellman key exchange
def diffie_hellman(p, g, private_key):
    public_key = power(g, private_key, p)
    return public_key

# Example usage
# Choose large prime numbers for p and g, and private keys for Alice and Bob
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Private keys for Alice and Bob
private_key_alice = 6
private_key_bob = 15

# Calculate public keys for Alice and Bob
public_key_alice = diffie_hellman(p, g, private_key_alice)
public_key_bob = diffie_hellman(p, g, private_key_bob)

# Shared secret key calculation
shared_secret_alice = power(public_key_bob, private_key_alice, p)
shared_secret_bob = power(public_key_alice, private_key_bob, p)

# Output
print("Public key for Alice:", public_key_alice)
print("Public key for Bob:", public_key_bob)
print("Shared Secret Key for Alice:", shared_secret_alice)
print("Shared Secret Key for Bob:", shared_secret_bob)
