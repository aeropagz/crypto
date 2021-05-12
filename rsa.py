from prime import generate_prime_number
from typing import List


def generate_rsa_modul(p: int, q: int):
    if p == q:
        raise ValueError("q must not equal p")
    return p * q


def euler(p: int, q: int):
    return (q - 1) * (p - 1)


def find_e(n: int):
    e = generate_prime_number(16)
    while True:
        if n % e == 0:
            e = generate_prime_number(16)
        else:
            break
    return e


def encrypt_string(msg: str, e: int, N: int) -> List[int]:
    cipher: List[int] = []
    for char in msg:
        cipher.append((ord(char) ** e % N))
    return cipher


def encrypt_number(i: int, e: int, N: int):
    return i ** e % N


def decrypt_string(cipher: List[int], d: int, N: int) -> str:
    msg: str = ""
    for i in cipher:
        msg += chr(pow(i, d, N))
    return msg


def decrypt_number(i: int, d: int, N: int):
    return i ** d % N
