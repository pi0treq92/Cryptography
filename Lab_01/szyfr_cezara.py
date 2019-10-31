"""
Before running the program please read file readme.txt.
Przed uruchomieniem programu proszę przeczytać plik readme.txt.
"""
from string import ascii_lowercase
slownik = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
           'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
           'z': 26}
slownik2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm',
            14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
            0: 'z'}
fileEncrypt = open("crypto.txt", 'r')
filePlain = open("plain.txt", "r")
fileKey = open("key.txt", "r")
klucz = fileKey.readline()
letters = ascii_lowercase
if len(klucz) > 2:
    kluczA = list(letters).index(klucz[0])
    kluczB = list(letters).index(klucz[2])
elif len(klucz) >0:
    kluczA = list(letters).index(klucz[0])
else:
    kluczA = None
    kluczB = None

def nwd(a, b):
	x, y = a, b
	while (y != 0):
		c = x % y
		x = y
		y = c
	return x

def NWD(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = NWD(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def szyfruj(plainText, b, a):
    zaszyfrowny = ""
    for i in range(len(plainText)):
        znak = list(letters).index(plainText[i])
        kod = (a*znak+b) % 26
        zaszyfrowny += list(letters)[kod]
    return zaszyfrowny

def deszyfruj(encryptText, b ,a):
    odszyfrowany = ""
    for i in range(len(encryptText)):
        znak = list(letters).index(encryptText[i])
        try:
            kod = (modinv(a, 26) * (znak - b)) % 26
        except:
            continue
        odszyfrowany += list(letters)[kod]
    return odszyfrowany

def tekstJawnyCezar(tekstJawny, encrypt):
    literaJawna = list(letters).index(tekstJawny[0])
    literaKod = list(letters).index(encrypt[0])
    if literaJawna>literaKod:
        a = 26 - (literaJawna-literaKod)
    elif literaJawna < literaKod:
        if (literaJawna + literaKod) > 26:
            a = 26 - (26 - (literaKod - literaJawna))
        else:
            a = literaKod - literaJawna
    return a

print("Witam w programie Szyfrowanie z Cezarem.")
print("Wybierz jedną z poniższyc opcji:\n'c':\tszyfr Cezara\n'a':\tszyfr afiniczny")
wybor = str(input())

print("Wybierz jedna z ponizszych opcji:\n'e':\tszyfrowanie\n'd':\todszyfrowanie\n'k':\tkryptoanaliza wyłacznie"
      " w oparciu o kryptogram\n'j':\tkryptoanaliza z tekstem jawnym")
wybor2 = str(input())
if wybor2.lower() == 'e':
            fileEncrypt = open("crypto.txt", 'w')
            plain = filePlain.read()
            if wybor == 'c':
                encrypt = szyfruj(plain, kluczA, 1)
            else:
                encrypt = szyfruj(plain, kluczA, kluczB)
            fileEncrypt.write(encrypt)
            fileEncrypt.close()
elif wybor2.lower() == 'd':
            fileDecrypt = open("decrypt.txt", 'w')
            encrypt = fileEncrypt.read()
            if wybor == 'c':
                decrypt = deszyfruj(encrypt, kluczA, 1)
            else:
                decrypt = deszyfruj(encrypt, kluczA, kluczB)
            fileDecrypt.write(decrypt)
            fileDecrypt.close()
elif wybor2.lower() == 'k':
            decrypt = ''
            fileDecrypt = open("decrypt.txt", 'w+')
            encrypt = fileEncrypt.read()
            if wybor == 'c':
                for i in letters:
                    klucz = list(letters).index(i)
                    decrypt += i + ':\t' + deszyfruj(encrypt, klucz, 1) + '\n'
                fileDecrypt.write(decrypt)
                fileDecrypt.close()
            else:
                tempTable = []
                for i in letters:
                    klucz = list(letters).index(i)
                    for j in range(1,26):
                        klucz2 = j
                        decrypt = 'a = ' + str(klucz+1) + ', b = ' + str(j) + ':\t' + deszyfruj(encrypt, klucz, j) + \
                                  '\n'
                        tempTable.append(decrypt)
                decrypt = ''
                for i in tempTable:
                    if len(i)>18:
                        decrypt+=i
                fileDecrypt.write(decrypt)
                fileDecrypt.close()

elif wybor2.lower() == 'j':
    newkeys = open("key-new.txt", 'w+')
    encrypt = fileEncrypt.read()
    plain = filePlain.read()
    if wybor == 'c':
        kod = tekstJawnyCezar(plain, encrypt)
        print('Kluczem szyfru jest: {}'.format(letters[kod]))
    else:
        if (len(encrypt) < len(plain)):
            length = len(encrypt)
        else:
            length = len(encrypt)
        wyniki = set()
        for i in range(length):
            wynik = set()
            for a in range(26):
                if nwd(a, 26) == 1:
                    for b in range(26):
                        if deszyfruj(encrypt[i], a, b) == plain[i]:
                                wynik.add((a, b))
            if len(wyniki) == 0:
                for i in wynik:
                    wyniki.add(i)
            else:
                wyniki = wyniki & wynik
        if len(wyniki) == 1:
            (a, b) = wyniki.pop()
            tekst = '{} {}'.format(letters[a], letters[b])
            newkeys.write(tekst)
