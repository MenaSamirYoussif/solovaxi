#========= Database interface ==========#

import sqlite3
import csv
from datetime import datetime ,timedelta ,date
from tabulate import tabulate
tabulate.PRESERVE_WHITESPACE = True

conn = sqlite3.connect('vdb.db')
c = conn.cursor()


def insert(ID, Name, Birth, Tel, Email, Address, Vaccine, Dose, Center, State, Date):
    c.execute("INSERT INTO vtable VALUES (NULL, ?, ?, ?, ?,?,?,?,?,?,?,?)",(ID, Name, Birth, Tel, Email, Address, Vaccine, Dose, Center, State, Date))
    conn.commit()

def find_name():
    name = str(input('Name : ' ,))
    c.execute("SELECT  CID, ID, Name, Tel, Email, Address FROM vtable WHERE Name LIKE ?",('%'+name+'%',))
    rows=c.fetchall()
    print(tabulate(rows, headers=["CID","ID","Name","Tel","Email","Address"] ))


def find_cid():
    cid = str(input('CID : ' ,))
    c.execute("SELECT * FROM vtable WHERE CID LIKE ?",('%'+cid+'%',))
    rows=c.fetchall()
    return rows

def find_cid_exact(): # This is for Generate PDF & QR
    rows = ['tst']
    cid = str(input('CID : ' ,))
    c.execute(" SELECT * FROM vtable WHERE CID = ? " ,(cid,))
    rows=c.fetchall()
    #print(tabulate(rows, headers=["CID","ID","Name","Birth","Tel","Email","Address","Vaccine", "Dose", "Center", "State", "Date"] ,  tablefmt="plain"))

    if len(rows) == 0 :
        CID      = None
        ID       = None
        Name     = None
        Birth    = None
        Tel      = None
        Email    = None
        Address  = None
        Vaccine  = None
        Dose     = None
        Center   = None
        State    = None
        Date     = None

        #print( CID, ID, Name)

    else :
        CID       = rows[0][0]
        ID        = rows[0][1]
        Name      = rows[0][2]
        Birth     = rows[0][3]
        Tel       = rows[0][4]
        Email     = rows[0][5]
        Address   = rows[0][6]
        Vaccine   = rows[0][7]
        Dose      = rows[0][8]
        Center    = rows[0][9]
        State     = rows[0][10]
        Date      = rows[0][11]
    

    return CID, ID, Name, Birth, Tel, Email, Address, Vaccine, Dose, Center, State, Date
    

    
    
    #return rows

    

def find_id():####################################################
    id = str(input('ID : ' ,))
    c.execute("SELECT  CID, ID, Name, Tel, Email, Address FROM vtable WHERE ID LIKE ?",('%'+id+'%',))
    rows=c.fetchall()
    print(tabulate(rows, headers=["CID","ID","Name","Tel","Email","Address"] ))


def get_certificate():
    Tel = str(input('Tel: ' ,))
    c.execute("SELECT  CID, ID, Name, Tel, Email, Address FROM vtable WHERE Tel LIKE ?",('%'+Tel+'%',))
    rows=c.fetchall()
    print(tabulate(rows, headers=["CID","ID","Name","Tel","Email","Address"] ))
    return rows

def find_tel():
    Tel = str(input('Tel: ' ,))
    c.execute("SELECT  CID, ID, Name, Tel, Email, Address FROM vtable WHERE Tel LIKE ?",('%'+Tel+'%',))
    rows=c.fetchall()
    print(tabulate(rows, headers=["CID","ID","Name","Tel No","Email","Address"] ))
    return rows
    
    




if  __name__ == "__main__":
    #get_certificate()
    #find_name()
    #find_id()
    find_cid_exact()

    
    


# c.close()

#print(find_cid_exact())

