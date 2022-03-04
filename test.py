from main import generate_key_pair, encrypt, decrypt

[d, e, n] = generate_key_pair()

c = encrypt(e, n, "Hello 🤣")
print(c)
print(decrypt(d, n, c))
