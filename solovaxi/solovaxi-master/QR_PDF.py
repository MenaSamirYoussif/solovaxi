#========= PDF/QR ==========#

import cleaner
import  DBI
import cv2
from fpdf import FPDF
import qrcode
import pyqrcode
from PIL import Image
import os
from datetime import date

time_stamp = date.today()



    



def make_qr_pdf():

        CID, ID, Name, Birth, Tel, Email, Address, Vaccine, Dose, Center, State, Date = DBI. find_cid_exact()


        data ='''
Cerificate  :{}
ID          :{}
Name        :{}
Vaccine     :{}
Dose        :{}
Center      :{}
Date        :{}
State       :{}
'''.format(CID, ID, Name,Vaccine,Dose, Center,Date,State,)

        print(data)
        img = qrcode.make(data)
    # bitimg = img.tobitmap()
    #os.mkdir('OUTPUT')
        
              
        img.save('OUTPUT\{}.png'.format(CID))
        cleaner.clean_folder()
        img.save('Temp\{}.png'.format(CID))
        #return CID


        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15 )
        pdf.image('Resources\svn.png', x = 15, w = 15, h = 15)#logo
        pdf.cell(100, 10, txt = 'CODEX - SOLOVAXI |  Generated  {}'.format(time_stamp), ln = 1)
        qrd = str('Temp\{}.png'.format(CID))
        pdf.image(qrd, x = 50 , w = 100, h = 100 )
        #txt
        pdf.cell(100, 10, txt = 'Cerificate   : {} '.format(CID), ln = 1)
        pdf.cell(100, 10, txt = 'ID              : {}'.format(ID) , ln = 1)
        pdf.cell(100, 10, txt = 'Name        : {}'.format(Name) , ln = 1)
        pdf.cell(100, 10, txt = 'Vaccine     : {}'.format(Vaccine)  , ln = 1)
        pdf.cell(100, 10, txt = 'Dose        : {}' .format(Dose), ln = 1)
        pdf.cell(100, 10, txt = 'Center      : {}' .format(Center), ln = 1)
        pdf.cell(100, 10, txt = 'Date         : {}' .format(Date), ln = 1)
        pdf.cell(100, 10, txt = 'State        : {}' .format(State), ln = 1)
        pdf.output('OUTPUT\{}.pdf'.format(CID))
        cleaner.clean_folder()

    






if  __name__ == "__main__":
    make_qr_pdf()
   
