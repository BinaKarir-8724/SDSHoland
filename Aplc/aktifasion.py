#!usr/bin/env python

import csv
import os
import platform
import pathlib


class getId():
# class to get ID of HDD

    def __init__(self):
#         super(getId,self).__init__()
        self.__check_os()
        pass
    
    def __check_os(self):
        
        if platform.system() == 'Windows':
            self.myIDHw = os.popen('vol ' + 'c:', 'r').read_file()
            self.myIDHw = self.myIDHw.split()
            self.myIDHw[len(self.myIDHw) - 1:]
            print (self.test[len(self.myIDHw) - 1:])
            print (platform.system())
       
        elif platform.system() == 'Linux':
            self.myIDHw = platform.system()
#             print (platform.system())

        return self.myIDHw

    def resultIDHDW(self):
#         print ("hee")
#         print (self.myIDHw)
        self.myIDHw = [self.myIDHw]
    
        return self.myIDHw


a = getId()
a.resultIDHDW()


class csvfile(getId):

    def __init__(self):
        super(csvfile, self).__init__()
        self.file = 'tk.py'
        pass

    def checkfile(self):
        self.file = pathlib.Path(os.getcwd() + "/tk.py")
        print (self.file)
        if self.file.is_file():
            self.read_file()
            self.result = "file is exist"
        else :
            self.result = "file not exist"
        return self.result

    def read_file(self):
        with open("tk.py", 'r') as csvfile:
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
    
    
if __name__ == "__main__":
    k = csvfile()
    print (k.checkfile())
    j = csvfile()
    print (j.write())
#     j.resultIDHDW()
