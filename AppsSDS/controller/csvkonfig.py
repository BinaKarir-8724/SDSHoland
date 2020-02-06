'''
Created on Jan 4, 2019

@author: binakarir
'''
import csv
import pathlib
import os
import sys
# 

 
class CSV():
    '''
    classdocs
    '''
 
    def __init__(self, parent, parent2):
        self.namepath = parent
        self.CSVFile = parent2
        self.listdb = []
        
    def __read(self):
        try :     
            self.f = open(self.namepath, "r")
            self.reader = csv.reader(self.f)
            for row in self.reader:
                self.listdb.append(row)
            self.f.close()
            return self.listdb
        except FileNotFoundError as F:
            print (F)
        
    def readdb(self):
        return self.__read()

        
if __name__ == "__main__":
    try :
        namedb = "listdb.txt"
        namePath = pathlib.Path(os.getcwd() + "/{}".format(namedb))  # "/AppsSDS/controller/{}".format(namedb))
        print (namePathd)
        tes = CSV(namePath, csv)
        k = tes.readdb()
        print (k[0][0])
    except  IndexError  as Val:
        print (Val)
        
