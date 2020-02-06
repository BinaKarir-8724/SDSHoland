'''
Created on Feb 5, 2019

@author: binakarir
'''

from AppsSDS.controller.controlvalue import CircleValue


class Riasec(object):
    
    def __init__(self, parent):
        self.parent = parent
        
        self.RIASEC = {
                        "R" : self.parent.sumscoresR,
                        "I" : self.parent.sumscoresI,
                        "A" : self.parent.sumscoresA,
                        "S"    : self.parent.sumscoresS,
                        "E"    : self.parent.sumscoresE,
                        "C" : self.parent.sumscoresC
                       }
         
        self.appCircle = CircleValue(**self.RIASEC)
 
        self.HasilHitung, self.HasilHitung2, self.ListHasilHitungS = self.appCircle.hasilhitung()
 
        try:
            self.riasec0 = []
            self.riasec1 = []
            for self.ListHasilHitung in self.ListHasilHitungS:
                self.riasec0.append(self.ListHasilHitung[0])
                self.riasec1.append(str(self.ListHasilHitung[1]))
             
            if self.riasec0 == ["N"] or self.riasec0 == ["None"]:
                self.riasec0.remove("N")
                self.riasec0.append("Anda belum Meng-Klik Hitung")
 
            print ("".join(self.riasec0))
            print ("".join(self.riasec1))
 
        except:
            self.result0 = "None"
            self.result1 = "None"
         
            pass
        self.result0 = "".join(self.riasec0)
        self.result1 = "".join(self.riasec1)
        self.riasec = [self.result0]  # ,self.result1]
 
        self.m_panelPage6.m_stHasil1.SetLabel(self.riasec[0])
         
        from AppsSDS.controller.sequence import CalculationRIASEC
        self.dataA = {
                        "R" : self.nilai_RealisticA,
                        "I" : self.nilai_InvestigativeA,
                        "A" : self.nilai_ArtisticA,
                        "S" : self.nilai_SocialA,
                        "E" : self.nilai_EnterprisingA,
                        "C" : self.nilai_ConventionalA 
                    }
        self.dataK = {
                        "R" : self.nilai_RealisticK,
                        "I" : self.nilai_InvestigativeK,
                        "A" : self.nilai_ArtisticK,
                        "S" : self.nilai_SocialK,
                        "E" : self.nilai_EnterprisingK,
                        "C" : self.nilai_ConventionalK 
                    }
        self.dataP = {
                        "R" : self.nilai_RealisticK,
                        "I" : self.nilai_InvestigativeK,
                        "A" : self.nilai_ArtisticK,
                        "S" : self.nilai_SocialK,
                        "E" : self.nilai_EnterprisingK,
                        "C" : self.nilai_ConventionalK 
                    }
        self.dataPD = {
                "R" : self.nilai_Kmekanisb1,
                "I" : self.nilai_Kilmiahb1,
                "A" : self.nilai_Kartistikb1,
                "S" : self.nilai_Kmengajarb1,
                "E" : self.nilai_Kpenjualan,
                "C" : self.nilai_Kadministrasib1 
                }
        self.dataPD2 = {
                "R" : self.nilai_Ktanganb2,
                "I" : self.nilai_Kmatematikab2,
                "A" : self.nilai_Kmusikb2,
                "S" : self.nilai_Moranglain,
                "E" : self.nilai_Kmanajerial,
                "C" : self.nilai_Kperkantoran 
                }
 
        self.riasecpersubA = CalculationRIASEC(**self.dataA)
        self.riasecpersubK = CalculationRIASEC(**self.dataK)
        self.riasecpersubP = CalculationRIASEC(**self.dataP)
        self.riasecpersubPD = CalculationRIASEC(**self.dataPD)
        self.riasecpersubPD2 = CalculationRIASEC(**self.dataPD2)
 
        self.riasecpersubA.SortRIASEC()
        self.riasecpersubK.SortRIASEC()
        self.riasecpersubP.SortRIASEC()
        self.riasecpersubPD.SortRIASEC()
        self.riasecpersubPD2.SortRIASEC()
     
        self.hasil_RIASECperSubA = self.riasecpersubA.SortRIASEC()
        self.hasil_RIASECperSubK = self.riasecpersubK.SortRIASEC()
        self.hasil_RIASECperSubP = self.riasecpersubP.SortRIASEC()
        self.hasil_RIASECperSubPD = self.riasecpersubPD.SortRIASEC()
        self.hasil_RIASECperSubPD2 = self.riasecpersubPD2.SortRIASEC()
        
        
