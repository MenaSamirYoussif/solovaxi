#======== SOLO Main ver 2.7 ======#

import Helper    
import DataEntry
import control
import DBI
import QR_PDF
import sys
import os

Helper.Help.ver() 


class Person: 
    
    def __init__(self):
        self.id         = None
        self.name       = None
        self.birth      = None
        self.tel        = None
        self.email      = None
        self.address    = None

    def set_person(self):
         self.id       = input('ID : ' ,)
         self.name  = input('Full Name : ',)

         print('Date Of Birth : ')
         
         self.birth   = DataEntry.DataEntry.date_entry()
         self.tel     = input('Tel :',)
         self.email   = input('Email : ',)
         self.address = input('Address : ' )




    def get_person(self):
        return  self.id, self.name, self.birth, self.tel, self.email, self.address
     





class Vaccinate: 
    
    def set_vaccine(self):
        Helper.Help.help_vaccine()
        self.__vaclst = ['Johnson & Johnson (LOT-123)','Pfizer (LOT-123)','AstraZeneca (LOT-123)','Moderna (LOT-123)']

        try :
            self.select = int(input('Vaccine : ' ,))
            if self.select in range(1,5):
                self.vac = self.__vaclst[self.select -1 ]
                return self.vac

            else:
                print('PLease choose option 1 to 4')
                Vaccinate.set_vaccine(self)

        except ValueError:
            print("Please Choose from option Numbers")
            Vaccinate.set_vaccine(self)

    def get_vaccine(self):
        return self.vac

    def set_dose(self):
        Helper.Help.help_dose()
        self.__doslst  = ['First Dose','Seconed Dose']

        try :
            self.select = int(input('Dose : ' ,))
            if self.select in range (1,3):
                 self.dose  = self.__doslst[self.select - 1]

            else:
                 print("Please chooose with options")
                 Vaccinate.set_dose(self)

        except ValueError:
            print("Please Choose from option Numbers")
            Vaccinate.set_dose(self)

                 

      


         
class VaccineCenter:       

    def set_center(self):
        
        Helper.Help.help_centr() 
        
        self.CenterName = input('Center : ',)
        self.state      = input('state: ',)
        self.date       = DataEntry.DataEntry.date_entry()
        

    def get_center(self):
        return self.CenterName , self.state, self.date



    

class Certificate(VaccineCenter, Vaccinate, Person): #===== all inherted to class Certifiacate===========#

    def __init__(self):
        VaccineCenter.__init__(self)
        Vaccinate.__init__(self)
        Person.__init__(self)
        
        
    def certification():
        print('Certificate Generated')

    
  
        

        
    



#=============== MAIN ==================#




if  control.access() == '%74521$co#':

    def main():
    
        certificate = Certificate()

        while True:
            try:
                Helper.Help.help_main()
                choice = int(input ('Plase Choose : ' , ))

                if choice == 1 :
                    certificate.set_person()
                    certificate.set_vaccine()
                    certificate.set_dose()
                    certificate.set_center()

                    DBI.insert(certificate.get_person()[0],certificate.get_person()[1], \
                               certificate.get_person()[2],certificate.get_person()[3], \
                               certificate.get_person()[4],certificate.get_person()[5], \
                               certificate.get_vaccine(),certificate.dose,certificate.get_center()[0],\
                               certificate.get_center()[1],certificate.get_center()[2])
                               
                
                elif choice == 2 : # Generate / Verify Certificate (CID)
                    print('Please Enter Certificate Numebr to Verviy and Generate QR / PDF Copy')
                    QR_PDF.make_qr_pdf()

                elif choice == 3 :
                    Helper.Help.help_query()

                    try :
                        qur = int(input('Choose Query By : ',))

                        if qur  in range(1,5):
                            if qur == 1:
                                DBI.find_name()

                            elif qur == 2 :
                                DBI.find_tel()

                            elif qur == 3 :
                                DBI.find_id()

                            elif qur == 4 :
                                main()
                            
                            

                        else :
                            print('Please choose form avialabe option')

                    except ValueError:
                            print("Please Choose from option Numbers")
                     
                elif choice == 4 :
                    sys.exit()

                else :
                    print('Unkowen Request . Please choose within options')

            except ValueError:
                    print("Please Choose from option Numbers")


    if __name__ == '__main__':
        main()


else:
    sys.exit()
