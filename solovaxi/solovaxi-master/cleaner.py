#========= folder cleaner ===========#
import os

def clean_folder():
    files =  os.listdir('Temp')
    for f in files:
        #print(type(f))
        os.remove('Temp\{}'.format(f))

clean_folder()
