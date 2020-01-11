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
        if len(bitString) % 4 == 0:
            bitTable.append(bitString)
            bitString = ''
    for j in range(len(bitTable)):
        decrypt += hex(int(bitTable[j], 2))[2]
    cryptoFile = open('detect.txt', 'w')
    cryptoFile.write(decrypt)
    cryptoFile.close()

def wynurz2():
    with open('watermark.html') as inf:
        txt = inf.read()
    docPlain = bs4.BeautifulSoup(txt, features="html.parser")
    paragraphCounter = 0
    crypto = ''
    check = False
    for j in range(paragraphCounter, len(docPlain.find_all('p'))):
        if crypto.__len__() >= 256:
            break
        else:
                counter = 0
                if docPlain.find_all('p')[j].string != None:
                        for k in range(counter, len(docPlain.find_all('p')[j].string)):
                            if check == True:
                                check = False
                                continue
                            if len(docPlain.find_all('p')[j].string) <= counter:
                                counter = 0
                                break
                            counter += 1
                            if docPlain.find_all('p')[j].string[k] == ' ':
                                try:
                                    if docPlain.find_all('p')[j].string[k+1] == ' ':
                                        crypto += '1'
                                        check = True
                                        continue
                                    else:
                                        crypto += '0'
                                        continue
                                except:
                                    continue
                            else:
                                continue
    decrypt = ''
    if len(crypto) > 256:
        crypto = crypto[:256]
    split_list = [crypto[x:x + 4] for x in range(0, len(crypto), 4)]
    for i in range(len(split_list)):
        decrypt += hex(int(split_list[i], 2))[2]
    cryptoFile = open('detect.txt', 'w')
    cryptoFile.write(decrypt)
    cryptoFile.close()

def zanurz2():
    cryptoFile = open('mess.txt', 'r')
    crypto = cryptoFile.readline()
    with open('cover.html') as inf:
        txt = inf.read()
    docPlain = bs4.BeautifulSoup(txt, features="html.parser")
    a = char2bits(crypto)
    counter = 0
    paragraphCounter = 0
    body = ''
    done = 0
    for i in range(len(a)):
        if a[i] == '1':
            for j in range(paragraphCounter, len(docPlain.find_all('p'))):
                if done == 1:
                    done = 0
                    break
                if docPlain.find_all('p')[j].string!= None:
                    if len(docPlain.find_all('p')[j].string) <= counter:
                        counter = 0
                        docPlain.find_all('p')[paragraphCounter].string = body
                        paragraphCounter += 1
                        body = ''
                        break
                    else:
                        for k in range(counter, len(docPlain.find_all('p')[j].string)):
                            if len(docPlain.find_all('p')[j].string) <= counter:
                                counter = 0
                                docPlain.find_all('p')[paragraphCounter].string = body
                                paragraphCounter += 1
                                body = ''
                                break
                            counter += 1
                            if docPlain.find_all('p')[j].string[k] ==' ':
                                docPlain.find_all('p')[j].string[k].replace(' ', '  ')
                                body += '  '
                                done = 1
                                break
                            else:
                                body += docPlain.find_all('p')[j].string[k]
        else:
            for j in range(paragraphCounter, len(docPlain.find_all('p'))):
                if done == 1:
                    done = 0
                    break
                if docPlain.find_all('p')[j].string != None:
                    if len(docPlain.find_all('p')[j].string) <= counter:
                        counter = 0

                        docPlain.find_all('p')[paragraphCounter].string = body
                        paragraphCounter += 1
                        body = ''
                        break
                    else:
                        for k in range(counter, len(docPlain.find_all('p')[j].string)):
                            if len(docPlain.find_all('p')[j].string) <= counter:
                                counter = 0

                                docPlain.find_all('p')[paragraphCounter].string = body
                                paragraphCounter += 1
                                body = ''
                                break
                            counter += 1
                            body += docPlain.find_all('p')[j].string[k]
                            if docPlain.find_all('p')[j].string[k] == ' ':
                                done = 1
                                break
    docPlain = [item for item in str(docPlain).split('\n') if item != '']
    watermarkFile = open('watermark.html', 'w')
    watermarkFile.writelines(["%s\n" % item for item in docPlain])
    watermarkFile.write(str(docPlain))

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
        if sys.argv[2] == '-1':
            zanurz()
        elif sys.argv[2] == '-2':
            zanurz2()
    elif sys.argv[1] == '-d':
        if sys.argv[2] == '-1':
            wynurz()
        elif sys.argv[2] == '-2':
            wynurz2()

main()
cryptoFile = open('mess.txt', 'r')
crypto = cryptoFile.readline()
a = char2bits(crypto)
print(a.__len__())