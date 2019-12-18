import sys, codecs, bs4

def char2bits(str):
    plainSign = "".join([bin(int(c, 16))[2:].zfill(4) for c in str])
    return plainSign

def wynurz():
    with open('watermark.html') as inf:
        txt = inf.readlines()
    bitTable = []
    bitString = ''
    decrypt = ''
    for i in range(256):
        if txt[i][-2] == ' ':
            bitString += '1'
        else:
            bitString += '0'
        if len(bitString)%4 == 0:
            bitTable.append(bitString)
            bitString = ''
    for j in range(len(bitTable)):
        decrypt += hex(int(bitTable[j], 2))[2]
    cryptoFile = open('detect.txt', 'w')
    cryptoFile.write(decrypt)
    cryptoFile.close()

def zanurz():
    with open('cover.html') as inf:
        txt = inf.read()
    docPlain = [item for item in str(bs4.BeautifulSoup(txt, features="html.parser")).split('\n') if item != '']
    cryptoFile = open('mess.txt', 'r')
    crypto = cryptoFile.readline()
    a = char2bits(crypto)
    for i in range(len(a)):
        if a[i] == '1':
            docPlain[i] += ' '
        else:
            pass
    watermarkFile = open('watermark.html', 'w')
    watermarkFile.writelines(["%s\n" % item for item in docPlain])

def main():
    if sys.argv[1] == '-e':
        zanurz()
        wynurz()
    elif sys.argv[1] == '-d':
        wynurz()

main()
cryptoFile = open('mess.txt', 'r')
crypto = cryptoFile.readline()
a = char2bits(crypto)
print(a.__len__())