hashFile = open("hash.txt", 'r')
hashes = hashFile.readlines()
def divideHashes(hashes):
    hashpersonal = [x for x in hashes[0:len(hashes)-1:2]]
    hashpersonal_ = [x for x in hashes[1:len(hashes):2]]
    return hashpersonal, hashpersonal_


hashpersonal, hashpersonal_ = divideHashes(hashes)

def prepareBin(hash):
    binTable = []
    for i in range(len(hash)):
        binar = []
        for j in range(len(hash[i])):
            if hash[i][j] != ' ':
                binar.append(bin(int(hash[i][j], 16))[2:].zfill(4))
            else:
                break
        binTable.append(binar)
    return binTable

def prepareString(l1):
    lstring = ''
    for i in range(len(l1)):
            lstring+=l1[i]
    return lstring

def compare(preparel1, preparel2, index, hashesPersonal, hashesPersonal_):
    string = ''
    counter = 0
    table = ["md5sum", "sha1sum", "sha224sum", "sha256sum", "sha384sum", "sha512sum"]
    for i in range(len(preparel1)):
        if preparel1[i] != preparel2[i]:
            counter+=1
        else:
            continue
    string = "\ncat hash.pdf personal.txt | {}\ncat hash.pdf personal_.txt | {}\n{}\n{}\n".format(table[index], table[index],
                                                                                       hashesPersonal[:-4], hashesPersonal_[:-4])
    string+="Liczba roznych bitow {}/{}, {}% wszystkich bitow\n".format(counter, len(preparel1), int((counter/len(preparel1))*100))
    return string

def compareHashes(hash1, hash2, hashes):
    string = ''
    if len(hash1) != len(hash2):
        raise ValueError("Length of hashes are not equal")
    else:
        counter = 0
        for i in range(len(hash1)):
            hashString1 = prepareString(hash1[i])
            hashString2 = prepareString(hash2[i])
            if len(hash1[i]) != len(hash2[i]):
                raise ValueError("Length of hashes are not equal")
            else:
                string+=compare(hashString1, hashString2, counter, hashes[counter], hashes[counter+1])
            counter += 1
    return string
def main():
    diff = open("diff.txt", 'w')
    personal = prepareBin(hashpersonal)
    personal_ = prepareBin(hashpersonal_)
    diff.write(compareHashes(personal, personal_, hashes))
    diff.close()

if __name__ == "__main__":
    main()

