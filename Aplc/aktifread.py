#!usr/bin/env python

import csv


class AktifChanel():
    
    def __init__(self):
        
        pass
    
    def check_aktivasi(self):
        
        pass
    
    def create_aktif(self):
        
        return

    def read_aktif(self):
        with open('tk.py', 'r') as readFile:
            reader = csv.reader(readFile)
            lines = list(reader)        
            print (lines)
        readFile.close()
        
        return lines
    

class csvfile():

    def __init__(self, parent):
        self.file = 'date.py'
        self.inputfile = parent
        pass

    def checkfile(self, check):
        self.filecheck = check
        print (self.filecheck)
        self.get_file()
        print (self.get_file())
#         print (self.l)
        if self.get_file() == self.filecheck:
            self.result = True
        else :
            self.result = False
        return self.result

    def read_file(self):
        with open("date.py", 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                self.l = ''.join(row)
#                 print (self.l)
        csvfile.close()
        return self.l
    
    def get_file(self):
        with open("date.py", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            self.lines = list(reader)
            self.lines[1]
            self.kondisi = "ada"
            
#             for row in spamreader:
#                 self.l = ''.join(row)
# #                 print (self.l)
        csvfile.close()
        return self.lines[1][0]
       
    def write(self, passwdch, datech):
        passwdch = [passwdch]
        datech = [datech]
#         print ([row])
#         row = ['jjkjskdfjl']
        
        try:       
            with open('date.py', 'r') as readFile:
                reader = csv.reader(readFile)
                lines = list(reader)
                lines[0] = datech
                lines[1] = passwdch
                    
            with open('date.py', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
    
            readFile.close()
            writeFile.close()
        except:
            lines = [["1"], ["1"]]
            with open('date.py', 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(lines)
                
            writeFile.close()            
            
            self.inputfile = [""]
        return lines[0][0], lines[1][0]
    

class FileDate():
    
    def __init__(self):
        
        pass
    
    def check_date(self):
#         
#         row = [[self.inputfile]]
#         lines=row
#         print ([row])
#         row = ['jjkjskdfjl']
        try:
            with open('date.py', 'r') as readFile:
                reader = csv.reader(readFile)
                
                if '/' in readFile.read():
                    self.a = 1
                else :
                    self.a = 2
          
            readFile.close()
            
            with open('date.py', 'r') as readFile :
                reader = csv.reader(readFile)
                if self.a == 1:
                    self.lines = list(reader)
                    self.lines[0]
                    self.kondisi = "ada"
                else :
                    self.lines = list(reader)
                    self.lines[0] = "Belum ada"
                    self.kondisi = "tidak ada"    
            readFile.close()
        except:
            self.lines.append("Belum ada")
            self.kondisi = "tidak ada"
            
#             print ("file kosong")

        return self.lines[0], self.kondisi

    def check_password(self):
        try:
            with open('date.py', 'r') as readFile :
                reader = csv.reader(readFile)
                self.lines = list(reader)
                self.lines[1]
                self.kondisi = "ada"
            readFile.close()
        except:
            self.lines.append("")
            self.kondisi = "tidak ada"
            
#             print ("file kosong")

        return self.lines[1], self.kondisi

    
if __name__ == "__main__":
#     j = csvfile("admin")
# #     print (j.read_file())
#     print (j.write("22sfgsg","date"))
#     print (j.checkfile("admin"))
#     j.resultIDHDW()
#     runtest = FileDate()
#     print (runtest.check_password())
      run = AktifChanel()
      print (run.read_aktif)
