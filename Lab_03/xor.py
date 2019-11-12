import sys
from string import ascii_lowercase
from string import ascii_uppercase as uppercase
from operator import itemgetter
letters = ascii_lowercase

def prepare():
    origFile = open('orig.txt', 'r')
    plainFile = open('plain.txt', 'w+')
    orig = origFile.read()
    text = ''
    sign = 1
    seq = []
    for i in range(len(orig)):
            if orig[i].lower() in ascii_lowercase or orig[i] == ' ':
                text += orig[i].lower()
            if (text.__len__()) % 32 == 0:
                seq.append(text+'\n')
                text = ''
    plainFile.writelines(seq)
    plainFile.close()
    print(text.__len__())


def encrypt():
    keyFile = open('key.txt', 'r')
    plainFile = open('plain.txt', 'r')
    encryptFile = open('crypto.txt', 'w+')
    plain = plainFile.readlines()
    plainFile.close()
    key = keyFile.read()
    seq = []
    text = ''
    for i in range(len(plain)):
        if plain[i].__len__()>31:
            for j in range(len(key)):
                plainSign = bin(ord(plain[i][j]))
                keySign = bin(ord(key[j]))
                y = int(plainSign, 2) ^ int(keySign, 2)
                text+=bin(y)[2:].zfill(8) + ' '
            seq.append(text+'\n')
            text = ''
    encryptFile.writelines(seq)


def xor(string):
    x = int(string, 2)
    y = int('00100000', 2)
    return x ^ y


def compare(jList, binTable, i):
    if jList.__len__() > 1:
        if binTable[jList[0]][i] == binTable[jList[1]][i] and  binTable[jList[0]][i] ==  binTable[jList[2]][i]:
            return True


def decrypt(table):
    klucz = {}
    for i in range(32):
        counter = 0
        jList = []
        for j in range(len(table)):
            if table[j][i][:3].__contains__('010'):
                counter += 1
                jList.append(j)
        if counter >= int(len(table)/3):
                 klucz[i] = int('00100000', 2)
        elif counter>1 and counter<int(len(table)/3):
                 if compare(jList, table, i):
                     klucz[i] = xor(table[jList[0]][i])
        else:
            klucz[i] = '00000000'
    return klucz


def cryptoanalysis():
    cryptoFile = open('crypto.txt', 'r')
    keyCrypto = open('key-crypto.txt', 'w')
    decryptFile = open('decrypt.txt', 'w')
    crypto = cryptoFile.readlines()
    cryptoFile.close()
    binTable = []
    bin = ''
    for i in range(len(crypto)):
        seq = []
        for j in range(len(crypto[i])):
            if crypto[i][j] != ' ':
                if crypto[i][j] != '\n':
                    bin += crypto[i][j]
            else:
                seq.append(bin)
                bin = ''
        binTable.append(seq)
    klucz = decrypt(binTable)
    decryptedKey = ''
    for key, value in klucz.items():
        try:
            decryptedKey += str(chr(value))
        except:
            decryptedKey +='?'
    print(decryptedKey)
    keyCrypto.write(decryptedKey)


def main():
    if sys.argv[1] == '-p':
        prepare()
    elif sys.argv[1] == '-e':
        encrypt()
    elif sys.argv[1] == '-k':
        cryptoanalysis()


main()
