hashFile = open("hash.txt", 'r')
hashes = hashFile.readlines()
print(len(hashes))
def divideHashes(hashes):
    hashpersonal = [x for x in hashes[0:len(hashes)-1:2]]
    hashpersonal_ = [x for x in hashes[1:len(hashes) - 1:2]]
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

def compareHashes(hash1, hash2):
    if len(hash1) != len(hash2):
        raise ValueError("Length of hashes are not equal")
    else:
        for i in range(len(hash1)):


personal = prepareBin(hashpersonal)
personal_ = prepareBin(hashpersonal_)

