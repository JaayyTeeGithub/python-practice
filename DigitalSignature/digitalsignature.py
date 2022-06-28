import random
from hashlib import sha512


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


def rabinMiller(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True


def isPrime(num):
    if num < 2:
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
                 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
                 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
                 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
                 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
                 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
                 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
                 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
                 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    return rabinMiller(num)


def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if isPrime(num):
            return num


def generateKey(key_size):
    print('Generating p.')
    p = generateLargePrime(key_size)
    print("p:", p)
    print()
    print('Generating q.')
    q = generateLargePrime(key_size)
    print("q:", q)
    print()
    print("Generating n.")
    n = p * q
    print("n:", n)
    print()
    print('Generating e.')
    while True:
        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print("e:", e)
    print()
    print('Calculating d.')
    d = findModInverse(e, (p - 1) * (q - 1))
    print("d:", d)
    public_key = (n, e)
    private_key = (n, d)
    print()
    print('Public key:', public_key)
    print('Private key:', private_key)
    return public_key, private_key


def makeKeys(key_size):
    public_key, private_key = generateKey(key_size)
    return public_key, private_key


def Main():
    public_key, private_key = makeKeys(1024)
    print()
    print("Message sent: Spooky, I know.")
    message_sent = b"Message to be signed."
    print()
    print("Generating message hash.")
    message_hash = int.from_bytes(sha512(message_sent).digest(), byteorder='big')
    print(message_hash)
    n = public_key[0]
    d = private_key[1]
    e = public_key[1]
    digital_signature = pow(message_hash, d, n)
    print()
    print("Digital Signature:", hex(digital_signature))
    verification_hash = pow(digital_signature, e, n)
    print("Verification hash:", hex(verification_hash))
    if message_hash == verification_hash:
        print()
        print("Contents are valid!")
        print("Hashed message matches the verification hash!")


Main()
