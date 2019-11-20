import binascii, os.path, urllib, random
from Crypto.Cipher import AES
import urllib.request

class ECBPenguin(object):
    '''
    A penguin class
    '''
    def __init__(self, img_clr=""):
        if not img_clr:
            self.__demo_image__()
            self.img_clr = "tux_clear.bmp"
        else:
            self.img_clr = img_clr
        self.__get_header__()

    def __demo_image__(self):
        '''
        Downloads a TUX image compatible for this program: square and with size multiple of 16
        '''
        print ("Downloading image...")
        image = urllib.request.URLopener()
        image.retrieve("http://fp-games.googlecode.com/svn/trunk/CodeWeek1/graviTux/data/tux.bmp","tux_clear.bmp")

    def __get_sizes__(self, dibheader):
        # Get image's dimensions (at offsets 4 and 8 of the DIB header)
        DIBheader = []
        for i in range(0,80,2):
            DIBheader.append(int(binascii.hexlify(dibheader)[i:i+2],16))
        self.width = sum([DIBheader[i+4]*256**i for i in range(0,4)])
        self.height = sum([DIBheader[i+8]*256**i for i in range(0,4)])

    def __get_header__(self):
        '''
        Read BMP and DIB headers from input image and write them to output image
        '''
        f_in = open(self.img_clr, 'rb')
        # BMP is 14 bytes
        bmpheader = f_in.read(14)
        # DIB is 40 bytes
        dibheader = f_in.read(40)
        self.__get_sizes__(dibheader)
        self._bmpheader = bmpheader
        self._dibheader = dibheader
        f_in.close()

    def encrypt(self, img_enc = "tux_enc.bmp", key = bytes('0123456789abcdef', encoding='utf8')):
        '''
        Encrypt the my_penguin
        '''
        self.img_enc = img_enc
        f_in = open(self.img_clr, 'rb')
        f_out = open(img_enc, 'wb')
        f_out.write(self._bmpheader)
        f_out.write(self._dibheader)
        row_padded = (self.width * self.height * 3)
        image_data = f_in.read(row_padded)
        cleartext =  binascii.unhexlify(binascii.hexlify(image_data))

        # AES ECB mode
        mode = 2
        # Encryptor
        encryptor = AES.new(key, mode)

        # Perform the encryption and write output to file
        f_out.write(encryptor.encrypt(cleartext))
        f_in.close()
        f_out.close()

def main():
    my_penguin = ECBPenguin(img_clr="plain24bit.bmp")
    my_penguin.encrypt()

if __name__ == "__main__":
    main()