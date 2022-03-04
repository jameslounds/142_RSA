from binascii import hexlify, unhexlify
import random
from Crypto.Util import number

from operations import modular_exponentiate


def generate_key_pair(p=None, q=None):
    if p is None or q is None:
        p, q = get_random_prime(), get_random_prime()

    # Choose a random d such that p != 1 (mod d), and q != 1 (mod d)
    # That is, d is coprime to (p-1)*(q-1), so has an inverse mod (p-1)*(q-1)
    d = random.randint(3, 2**32)
    while gcd_extended(d, (p-1) * (q-1))[0] != 1:
        d = random.randint(3, 2**32)

    # Since d, (p-1)(q-1) are coprime, x is the modular multiplicative inverse of d mod (p-1)(q-1)
    [_, e, _] = gcd_extended(d, (p-1) * (q-1))

    n = p * q
    return [d, e, n]


def convert_string_to_message(string):
    return int.from_bytes(hexlify(string.encode("utf-8")), "little")


def convert_message_to_string(message):
    message_bytes = message.to_bytes((message.bit_length() + 7) // 8, "little")
    return unhexlify(message_bytes).decode("utf-8")


def encrypt(e, n, plain_text_string):
    plain_text_message = convert_string_to_message(plain_text_string)
    return modular_exponentiate(plain_text_message, e, n)


def decrypt(d, n, cipher_text_message):
    plain_text_message = modular_exponentiate(cipher_text_message, d, n)
    return convert_message_to_string(plain_text_message)


def gcd_extended(a, b):
    # Usage [_, d, _] = gcd_extended(e, (p-1)*(q-1)) will set variable d to decryptio exponent
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


def get_random_prime():
    return number.getPrime(512)
