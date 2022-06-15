#========== QR - Reader - utf-8 ==========#

print("=================== Codex QReader 1.7 ===========")

import cv2
from pyzbar.pyzbar import decode

def read_qr():
    while True :
        try:
            file = str(input(" File Name : ",))
            img = cv2.imread('{}.png'.format(file))
            for  QR in  decode(img):
                print(QR.data.decode('utf-8'))

        except TypeError:
             print('File Does not exsits Try Again')
             read_qr()
                
            
            
read_qr()
