#!usr/bin/python
# import os
import pathlib

import openpyxl


class Work_excel():
    
    def __init__(self):
        
        pass
    
    def get_data(self):
    
        filename = "dataof.xlsx"  # pathlib.Path.cwd() +
        print ("ll")
        filename = filename
        print (filename)
        
        workexcel = openpyxl.load_workbook(filename, read_only=False, keep_vba=True, data_only=True, \
                                guess_types=False, keep_links=True)
        workexcel.save(filename)
        listprofesion = {}
        print (listprofesion)
        listcell = 1520
        k = 1
        for i in range(listcell) :
            key = workexcel["Sheet1"]["A{}".format(k)].value
            valuess = workexcel["Sheet1"]["B{}".format(k)].value
            listprofesion[key] = valuess
            print (i)
            k += 1

#             listprofesion.update({key:value})
            print (key)
#         print (listprofesion.items())
        print (listprofesion)
        return listprofesion

    
r = Work_excel()
print ("jj")
r.get_data()
    
    # workexcel.get_named_range("Alphabetized Index")
