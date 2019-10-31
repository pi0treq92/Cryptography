import sys
from string import ascii_lowercase
from string import ascii_uppercase as uppercase
from operator import itemgetter

letters = ascii_lowercase
frequences = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074]


def cesar_cipher(letter, key):
    znak = list(letters).index(letter)
    b = list(letters).index(key)
    num = (znak + b) % 26
    encryptedLetter = list(letters)[num]
    return encryptedLetter


def prepare():
    origFile = open('orig.txt', 'r')
    plainFile = open('plain.txt', 'w')
    orig = origFile.read()
    text = ''
    for i in range(len(orig)):
        if orig[i].lower() in ascii_lowercase:
            text += orig[i].lower()
    plainFile.write(text)
    plainFile.close()
    print(text.__len__())


def encrypt():
    keyFile = open('key.txt', 'r')
    plainFile = open('plain.txt', 'r')
    encryptFile = open('crypto.txt', 'w')
    plain = plainFile.read()
    crypto = ''
    key = keyFile.read()
    letter = 0
    for i in range(len(plain)):
        letter = letter % len(key)
        crypto += cesar_cipher(plain[i], key[letter])
        letter += 1
    encryptFile.write(crypto)


def decrypt():
    keyFile = open('key.txt', 'r')
    decryptFile = open('decrypt.txt', 'w')
    encryptFile = open('crypto.txt', 'r')
    encrypt = encryptFile.read()
    decrypt = ''
    key = keyFile.read()
    letter = 0
    for i in range(len(encrypt)):
        letter = letter % len(key)
        sign = list(letters).index(encrypt[i])
        b = list(letters).index(key[letter])
        code = (sign - b) % 26
        decrypt += list(letters)[code]
        letter += 1
    decryptFile.write(decrypt)


def cryptoanalysis(target_freqs):
    crypto = open('crypto.txt', 'r')
    keyCrypto = open('key-crypto.txt', 'w')
    decryptFile = open('decrypt.txt', 'w')
    input = crypto.read()
    nchars = len(ascii_lowercase)
    ordA = ord('a')
    sorted_targets = sorted(target_freqs)

    def frequency(input):
        result = [[c, 0.0] for c in ascii_lowercase]
        for c in input:
            result[c - ordA][1] += 1
        return result

    def correlation(input):
        result = 0.0
        freq = frequency(input)
        freq.sort(key=itemgetter(1))

        for i, f in enumerate(freq):
            result += f[1] * sorted_targets[i]
        return result

    cleaned = [ord(c) for c in input.lower() if c.islower()]
    best_len = 0
    best_corr = -100.0

    for i in range(2, len(cleaned) // 10):
        pieces = [[] for _ in range(i)]
        for j, c in enumerate(cleaned):
            pieces[j % i].append(c)

        corr = -0.5 * i + sum(correlation(p) for p in pieces)

        if corr > best_corr:
            best_len = i
            best_corr = corr

    if best_len == 0:
        print("Text is too short to analyze")
        return "Text is too short to analyze", ""

    pieces = [[] for _ in range(best_len)]
    for i, c in enumerate(cleaned):
        pieces[i % best_len].append(c)

    freqs = [frequency(p) for p in pieces]

    key = ""
    for fr in freqs:
        fr.sort(key=itemgetter(1), reverse=True)

        m = 0
        max_corr = 0.0
        for j in range(nchars):
            corr = 0.0
            c = ordA + j
            for frc in fr:
                d = (ord(frc[0]) - c + nchars) % nchars
                corr += frc[1] * target_freqs[d]

            if corr > max_corr:
                m = j
                max_corr = corr

        key += chr(m + ordA)
    # Deszyfrowanie ze znalezionym kluczem
    r = (chr((c - ord(key[i % best_len]) + nchars) % nchars + ordA) for i, c in enumerate(cleaned))
    decrypt = "".join(r)
    decryptFile.write(decrypt)
    keyCrypto.write(key)


def main():
    if sys.argv[1] == '-e':
        encrypt()
    elif sys.argv[1] == '-p':
        prepare()
    elif sys.argv[1] == '-d':
        decrypt()
    elif sys.argv[1] == '-k':
        cryptoanalysis(frequences)


main()
