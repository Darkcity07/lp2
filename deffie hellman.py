def power(a, b, p):
    if b == 1:
        return a
    else:
        return (pow(a, b) % p)

# Driver program
p = 23  # A prime number P is taken
g = 9  # A primitive root for P, G is taken

# Alice chooses the private key a
a = 4  # a is the chosen private key
x = power(g, a, p)  # Gets the generated key

# Bob chooses the private key b
b = 3  # b is the chosen private key
y = power(g, b, p)  # Gets the generated key


# Generating the secret key after the exchange of keys
ka = power(y, a, p)  # Secret key for Alice
kb = power(x, b, p)  # Secret key for Bob

print("Secret key for Alice is:", ka)
print("Secret key for Bob is:", kb)