import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def power(a, b, p):
    if b == 1:
        return a
    else:
        return (pow(a, b) % p)

def rsa_encrypt(message, p, q, e):
    n = p * q
    z = (p - 1) * (q - 1)
    c = (message ** e) % n
    return c

def rsa_decrypt(ciphertext, p, q, d):
    n = p * q
    z = (p - 1) * (q - 1)
    message = (ciphertext ** d) % n
    return message

# Generate prime numbers p and q
p = 17
q = 23

# Calculate modulus n
n = p * q

# Calculate totient z
z = (p - 1) * (q - 1)

# Choose public key e such that gcd(e, z) = 1
e = 7

# Calculate private key d
d = 19

# Encrypt a message
message = 12345
ciphertext = rsa_encrypt(message, p, q, e)
print("Encrypted message:", ciphertext)

# Decrypt the ciphertext
decrypted_message = rsa_decrypt(ciphertext, p, q, d)
print("Decrypted message:", decrypted_message)