#!usr/bin/python
# import checkfile

# datainput = checkfile()

import csv
import os
# import platform
import pathlib


class CheckCSV():

    def __init__(self):
        super(CheckCSV, self).__init__()
        self.file = 'ckh.py'
        pass

    def checkfile(self):
        self.file = pathlib.Path(os.getcwd() + "/ckh.py")
        print (self.file)
        if self.file.is_file():
            self.read_file()
            self.result = "file is exist"
        else :
            self.result = "file not exist"
        return self.result

    def read_file(self):
        with open("ckh.py", 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                self.l = ''.join(row)
#                 print (self.l)
        csvfile.close()
        return self.l
       
    def write(self):
        
        row = [[self.myIDHw]]
        lines = row
#         print ([row])
#         row = ['jjkjskdfjl']
        '''        
        with open('tk.py', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)
            lines[1] = [row]
        '''        
        with open('tk.py', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

#         readFile.close()
        writeFile.close()

        return self.myIDHw
    
# datapassword = input ("Masukkan password")
# print(datapassword)

# if datapassword = checkfile():
#     print ("True")
# else :
#     print ("False")


tanggal = ["default"]
password = ["default"]

Keluar = 0
while Keluar == 0 :

# while True:
    class Setting():

        def __init__(self, parent, *args):
            self.set = parent
            self.tanggal = args[0]
            self.password = args[1]
 
            if self.set == "SetTgl":
                self.SetTgl()
            
            elif self.set == "SetPasswd":
                self.SetPasswd()
            
            elif self.set == "Keluar" :
                self.Keluar()
            
            elif self.set == "Lihat Konfigurasi":
                self.LihatKonf()

        def SetTgl(self):
            self.tanggaltambah = input ("set tanggal dd/mm/yyyy")
            del self.tanggal[0]
            return self.tanggal.append(self.tanggaltambah)
        
        def SetPasswd(self):
            print ("set password")
            self.passwordtambah = input (" Set Password")
            del self.password[0]
            return self.password.append(self.passwordtambah)
                
        def LihatKonf(self):
            print ("\n\nTanggal berakhir : {}".format(self.tanggal))
            print ("Password         : {}\n".format(self.password))
        
        def Keluar(self):
            global Keluar
            Keluar = 11
            
    if __name__ == "__main__":
        
        datatanggal = input ('silahkan pilih :\n'\
                        '1. Setting Tanggal\n2. Setting Password\n3. Keluar & Simpan\n4. Lihat Konfigurasi\n')
        dictionary = {"1":"SetTgl", "2":"SetPasswd", "3":"Keluar", "4":"Lihat Konfigurasi"}
        
#         print (dictionary.get(datatanggal,"Not Found"))
    
        k = dictionary.get(datatanggal, "Not Found")
        go = Setting(k, tanggal, password)
        
