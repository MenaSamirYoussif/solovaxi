#========= Data Entry ===========#

from datetime import datetime ,timedelta ,date

class DataEntry:
    def date_entry():

        try :
            Day = int (input ('Day: ' , ))
            Month = int (input ('Month: ' , ))
            Year = int (input ('Year: ' , ))
            Date = date(Year, Month, Day)
            return Date

        except ValueError:
            print('Entered Date out of normal date range or non numerical,  Try again')
            return DataEntry.date_entry()
            

#print(DataEntry.date_entry())




if  __name__ == "__main__":

    DataEntry.date_entry()
