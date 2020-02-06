

class CircleValue():
        
    def __init__(self, **args):
        self.dictofarguments = args
#         print("hello")
        self.__method()
        
#         print (self.__method())
        pass
    
    def __method(self):
        self.listkey = []
        self.listvalue = []
        self.i = 1
        self.k = 0
        self.sortevalue = sorted(self.dictofarguments.items(), key=lambda x: x[1], reverse=True)
        for key, value in dict(self.sortevalue).items():
#             print (key, value)
            self.listvalue.append(value) 
            self.listkey.append(key)
#         print (self.listkey)
#         print (self.listvalue)
        self.hasil = set([x for x in self.listvalue[0:5] if self.listvalue[0:5].count(x) > 1])
        self.hasila = set([x for x in self.listvalue[0:4] if self.listvalue[0:4].count(x) > 1])

        print (self.hasil) 

#         if self.hasil != self.hasila:
#             self.jk = 0 
#             
            
        if len(list(self.hasil)) > 1:
            print("data tidak valid, karena jumlah nilai yang sama "\
                  "ada {}".format(len(list(self.hasil))))
            self.a = 0
        elif len(list(self.hasil)) == 1 and len(list(self.hasila)) == 1 :
            print ('data valid karena jumlah nilai yang sama '\
                   "adalah {}".format(len(list(self.hasil))))
            self.a = 1
        
        else :
            print ("data valid karena jumlah nilai yang sama"\
                   " ada {}".format(len(list(self.hasil))))
            self.a = 2
            
#         for self.loopinga in range(0,len(self.sortevalue)-1)  :
#             if self.sortevalue[self.loopinga][1] == list(self.hasil)[0]:
#                 print (self.loopinga)
#                 self.hasilakhir = "None"
#                 self.hasilakhir2 = "None"
#                 self.loopingah=self.loopinga
#             else :
#                 pass
#         print (self.loopinga)
#         print (self.loopingah)
            
        try:
            if self.a == 0:
                self.hasilakhir = "Nav"
                self.hasilakhir2 = "Nav"   
                self.sortevalue = "None"
                self.hh = 11
            
            elif self.a == 1:
                self.sortevalue1 = self.sortevalue[0:4]
                self.sortevalue = self.sortevalue[0:4]
    
                self.list1 = self.sortevalue[0:4]
                self.list2 = self.sortevalue[0:4]
                for self.i in range(0, len(self.sortevalue) - 1):
                    if self.list1[self.i][1] == list(self.hasil)[0]:
    #                     print ("circle number {}".format(self.i))
                        print (self.sortevalue[self.i])
                        del self.list1[self.i + 1]
                        del self.list2[self.i]
                        print (self.list1)
                        print (self.list2)
                    else :
                        print("keluar kategori")
                        pass
                print (self.list1 , self.list2)
                self.hasilakhir = self.list1
                self.hasilakhir2 = self.list2
    #         
            elif self.a == 2 :
                print (self.sortevalue[0:3])
                self.hasilakhir = self.sortevalue[0:3]
                self.hasilakhir2 = ["None"]
                self.sortevalue = self.sortevalue[0:3]
        except:
            self.hasilakhir = "None"
            self.hasilakhir2 = "None"
            self.sortevalue = "None"
            pass
        print (self.sortevalue[0:4])
        print (len(list(self.hasil)))
        return self.hasilakhir, self.hasilakhir2, self.sortevalue
    
    def nn(self):
        
        return self.hh
    
    def hasilhitung(self):
        return self.hasilakhir, self.hasilakhir2, self.sortevalue
        #             
#         self.listvalue[0:3]
#         print (self.listvalue[0:4])
#         if len(self.hasil)==1:
#             print (self.listvalue[0:4])
#         elif len(self.hasil)>=1:
#             print ("hasil tidak valid")
#         elif len(self.hasil)==0:
#             print (self.listvalue[0:3])
#         
#         for i in range(len(self.listvalue[0:4])-1):
#             if self.listvalue[i]==self.listvalue[i+1]:
#                 print (self.listvalue[i])
                    
        return
        
        pass
    
    
if __name__ == '__main__':
    listargument = {"R":3, "I":3, "A":3, "S":2, "E":2, "C":8}

    tes = CircleValue(**listargument)
    print (tes.hasilhitung())
    HasilHitung, HasilHitung2, \
    HasilHitung3 = tes.hasilhitung()
    riasecv = []
    riaseck = []
    for hh in HasilHitung3:
        print (hh[0])
        riaseck.append(hh[0])
        riasecv.append(str(hh[1]))
    print ("".join(riaseck))
    print ("".join(riasecv))
#     HasilHitung = [x for x in HasilHitung]
    hasilhitungs = []
    for HasilHitung_e in HasilHitung:
        hasilhitungs.append(str(HasilHitung_e[0]))
    
    print ("".join(hasilhitungs))

    hasilhitungs2 = []
    for HasilHitung_e in HasilHitung2:
        hasilhitungs2.append(str(HasilHitung_e[0]))
    
    print ("".join(hasilhitungs2))

