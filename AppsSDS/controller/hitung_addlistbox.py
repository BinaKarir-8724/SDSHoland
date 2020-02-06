class NewClass(object):
    
    classname = 'listbox'
    # print (classname)
    
    def __init__(self, parent):
        self.parent = parent
        print("Aktivitas")
        self.listaktivitasA = (
                              "R = {}".format(self.parent.m_panelPage3.m_RealisticA.GetValue()), \
                              "I = {}".format(self.parent.m_panelPage3.m_InvestigativeA.GetValue()), \
                              "A = {}".format(self.parent.m_panelPage3.m_ArtisticA.GetValue()), \
                              "S = {}".format(self.parent.m_panelPage3.m_SocialA.GetValue()), \
                              "E = {}".format(self.parent.m_panelPage3.m_EnterprisingA.GetValue()), \
                              "C = {}".format(self.parent.m_panelPage3.m_ConventionalA.GetValue())\
                              )

    def __method(self):
        
        if not self.parent.m_panelPage5.m_lbaktivitas.GetCount() > 0:
            print ("Belum ada data yang dimasukkan")
            pass
                
        else :
            for index in range(0, self.parent.m_panelPage5.m_lbaktivitas.GetCount()):
                self.parent.m_panelPage5.m_lbaktivitas.Delete(0)
                
#         self.parent.m_panelPage5.m_lbaktivitas.InsertItems(self.listaktivitasA,0)
#         print(self.parent.m_panelPage5.m_lbaktivitas.GetCount())
    
    def resultlistbox(self):
        self.__method()
        return self.parent.m_panelPage5.m_lbaktivitas.InsertItems(self.listaktivitasA, 0)


class NewClass2(object):
    
    def __init__(self, parent):
        self.parent = parent
        print("Kompetensi")

        self.listaktivitasK = (
                              "R = {}".format(self.parent.m_panelPage3.m_RealisticK.GetValue()), \
                              "I = {}".format(self.parent.m_panelPage3.m_InvestigativeK.GetValue()), \
                              "A = {}".format(self.parent.m_panelPage3.m_ArtisticK.GetValue()), \
                              "S = {}".format(self.parent.m_panelPage3.m_SocialK.GetValue()), \
                              "E = {}".format(self.parent.m_panelPage3.m_EnterprisingK.GetValue()), \
                              "C = {}".format(self.parent.m_panelPage3.m_ConventionalK.GetValue())\
                              )

    def __method(self):
        if not self.parent.m_panelPage5.m_lbkompetensi.GetCount() > 0:
            pass
        else :
            for index in range(0, 6):
                self.parent.m_panelPage5.m_lbkompetensi.Delete(0)
                
    def resultlistbox(self):  
        self.__method()
        return self.parent.m_panelPage5.m_lbkompetensi.InsertItems(self.listaktivitasK, 0)
    

class NewClass3(object):
    
    def __init__(self, parent):    
        self.parent = parent
        print("Pekerjaan")

        self.listaktivitasP = (
                              "R = {}".format(self.parent.m_panelPage3.m_RealisticP.GetValue()), \
                              "I = {}".format(self.parent.m_panelPage3.m_InvestigativeP.GetValue()), \
                              "A = {}".format(self.parent.m_panelPage3.m_ArtisticP.GetValue()), \
                              "S = {}".format(self.parent.m_panelPage3.m_SocialP.GetValue()), \
                              "E = {}".format(self.parent.m_panelPage3.m_EnterprisingP.GetValue()), \
                              "C = {}".format(self.parent.m_panelPage3.m_ConventionalP.GetValue())\
                              )

    def __method(self):
        if not self.parent.m_panelPage5.m_lbpekerjaan.GetCount() > 0:
            print ("Belum ada data yang dimasukkan")
            pass
                
        else :
            for index in range(0, self.parent.m_panelPage5.m_lbpekerjaan.GetCount()):
                self.parent.m_panelPage5.m_lbpekerjaan.Delete(0)
    
    def resultlistbox(self):
        self.__method()
        print(self.parent.m_panelPage5.m_lbpekerjaan.GetCount())    

        return self.parent.m_panelPage5.m_lbpekerjaan.InsertItems(self.listaktivitasP, 0)
    
        
class NewClass4(object):
    
    def __init__(self, parent):
        self.parent = parent
        print("Penilaian Diri Bag 1")
        
        self.parent.m_panelPage4.m_kmekanisb1.GetValue()
        self.parent.m_panelPage4.m_kilmiahb1.GetValue()
        self.parent.m_panelPage4.m_kartistikb1.GetValue()
        self.parent.m_panelPage4.m_kmengajarb1.GetValue()
        self.parent.m_panelPage4.m_kpenjualanb1.GetValue()
        self.parent.m_panelPage4.m_kadministrasib1.GetValue()
 
        self.listaktivitasPD = (
                              "R = {}".format(self.parent.m_panelPage4.m_kmekanisb1.GetValue()), \
                              "I = {}".format(self.parent.m_panelPage4.m_kilmiahb1.GetValue()), \
                              "A = {}".format(self.parent.m_panelPage4.m_kartistikb1.GetValue()), \
                              "S = {}".format(self.parent.m_panelPage4.m_kmengajarb1.GetValue()), \
                              "E = {}".format(self.parent.m_panelPage4.m_kpenjualanb1.GetValue()), \
                              "C = {}".format(self.parent.m_panelPage4.m_kadministrasib1.GetValue())\
                              )

#         print(self.parent.m_panelPage5.m_lbpenilaianbag1.GetCount())
    def __method(self):
        
        if not self.parent.m_panelPage5.m_lbpenilaianbag1.GetCount() > 0:
             
            pass
         
        else :
            for index in range(0, 6):
#                 print (index)
                self.parent.m_panelPage5.m_lbpenilaianbag1.Delete(0)

    def resultlistbox(self):  
        self.__method()           
        print(self.parent.m_panelPage5.m_lbpenilaianbag1.GetCount())

        return self.parent.m_panelPage5.m_lbpenilaianbag1.InsertItems(self.listaktivitasPD, 0)
 

class NewClass5(object):
    
    def __init__(self, parent):
        self.parent = parent

        print("Penilaian Diri Bag 2")

        self.listaktivitasPD2 = (
                              "R = {}".format(self.parent.m_panelPage4.m_ktanganb2.GetValue()), \
                              "I = {}".format(self.parent.m_panelPage4.m_kmatematikab2.GetValue()), \
                              "A = {}".format(self.parent.m_panelPage4.m_kmusikb2.GetValue()), \
                              "S = {}".format(self.parent.m_panelPage4.m_moranglainb2.GetValue()), \
                              "E = {}".format(self.parent.m_panelPage4.m_kmanajerialb2.GetValue()), \
                              "C = {}".format(self.parent.m_panelPage4.m_kperkantoranb2.GetValue())\
                              )
        print(self.parent.m_panelPage5.m_lbpenilaianbag2.GetCount())
    
    def __method(self):
        if not self.parent.m_panelPage5.m_lbpenilaianbag2.GetCount() > 0:
            
            pass
        
        else :
            for index in range(0, 6):
                self.parent.m_panelPage5.m_lbpenilaianbag2.Delete(0)
                
    def resultlistbox(self):
        self.__method()
        print(self.parent.m_panelPage5.m_lbpenilaianbag2.GetCount())        
        
        return self.parent.m_panelPage5.m_lbpenilaianbag2.InsertItems(self.listaktivitasPD2, 0)
         
