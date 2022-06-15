#===== Help Class =====#


from datetime import date
time_stamp = date.today()

class Help:

    def ver():
        
        return print('SYS DATE : ', time_stamp, '''| Codex SOLOVAXI VER  2.7 (user: group7, password: seven7) |''')

    def help_main():
        return print('''
Main Options ========================================================
                       1. To Record Certifiacte
                       2. Generate / Verify Certificate (CID)
                       3. Query approximate (Name /  Tel  / ID)
                       4. Exit
                       ''')


    def help_vaccine():
        return print('''
Choose Vaccine ======================================================
                        1. Johnson & Johnson (LOT-123)
                        2. Pfizer (LOT-123)
                        3. AstraZeneca (LOT 123)
                        4. Moderna (LOT 123)
                        ''')



    def help_dose():
        return print('''
Choose Dose ========================================================
                        1. Frist Dose
                        2. Second Dose
                        ''')



    def help_centr():
        return print('''
Vaccine Center =====================================================''')


    def help_query():
        return print('''
Query Options =====================================================
                      1. Query by approximate name
                      2. Query by approximate Tel No
                      3. Query by ID Recodred in Certificate
                      4. Home (Main Options)
 


''')

    
