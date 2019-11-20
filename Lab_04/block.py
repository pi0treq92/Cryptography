import binascii, os.path, urllib, random
from PIL import Image
import subprocess

class cbcPenguin(object):
    def __init__(self, img_clr=""):
        if not img_clr:
            self.__demo_image__()
            self.img_clr = "letter-plain.bmp"
        else:
            self.img_clr = img_clr
        self.__get_header__()

    def __get_sizes__(self, dibheader):
        # Get image's dimensions (at offsets 4 and 8 of the DIB header)
        DIBheader = []
        for i in range(0,80,2):
            DIBheader.append(int(binascii.hexlify(dibheader)[i:i+2],16))
        self.width = sum([DIBheader[i+4]*256**i for i in range(0,4)])
        self.height = sum([DIBheader[i+8]*256**i for i in range(0,4)])

    def __get_header__(self):
        f_in = open(self.img_clr, 'rb')
        # BMP is 14 bytes
        bmpheader = f_in.read(14)
        # DIB is 40 bytes
        dibheader = f_in.read(40)
        self.__get_sizes__(dibheader)
        self._bmpheader = bmpheader
        self._dibheader = dibheader
        f_in.close()

    def show_clr(self):
        '''
        Display cleartext penguin
        '''
        im = Image.open(self.img_clr)
        im.show()

    def show_enc(self):
        '''
        Display ciphertext penguin
        '''
        im = Image.open(self.img_enc)
        im.show()

ca0 = "openssl "
cb0 = "dd if=letter-plain.bmp "

def imagencryptecb():
    cecba1 = "enc -aes-256-ecb -in letter-plain.bmp "
    cecba2 = "-out letter-ecb.bmp -pass pass:qwertyuiop"
    cecba = ca0 + cecba1 +  cecba2
    subprocess.getoutput(cecba)
    cecbb1 = "of=letter-ecb.bmp bs=1 "
    cecbb2 = "count=54 conv=notrunc"
    cecbb = cb0 + cecbb1 + cecbb2
    subprocess.getoutput(cecbb)

def imagencryptcbc():
    ccbca1 = "enc -aes-256-cbc -in letter-plain.bmp "
    ccbca2 = "-out letter-cbc.bmp -pass pass:qwertyuiop"
    ccbca = ca0 + ccbca1 +  ccbca2
    subprocess.getoutput(ccbca)
    ccbcb1 = "of=letter-cbc.bmp bs=1 "
    ccbcb2 = "count=54 conv=notrunc"
    ccbcb = cb0 + ccbcb1 + ccbcb2
    subprocess.getoutput(ccbcb)

    subprocess.getstatusoutput("openssl enc -aes-256-cbc -in letter-plain.bmp -out letter-cbc.bmp -pass pass:mypass")
    subprocess.getstatusoutput("dd if=letter-plain.bmp of=letter-cbc.bmp bs=1 count=54 conv=notrunc")


def main():
    imagencryptecb()
    imagencryptcbc()

if __name__ == "__main__":
    main()