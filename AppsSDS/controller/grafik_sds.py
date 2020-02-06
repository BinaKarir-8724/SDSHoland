'''
Created on Feb 5, 2019

@author: binakarir
'''


class Grafik1(object):
    
    def __init__(self, parent):
        self.parent = parent

        self.figure = self.parent.m_panelPage5.m_plotb.figure
        self.axes1 = self.figure.add_subplot(111)
        
        try:
            for a in range(0, 6):
                self.axes1.lines[0].remove()
        except:
            pass
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y1 = (self.parent.m_panelPage3.m_RealisticA.GetValue(), \
                self.parent.m_panelPage3.m_InvestigativeA.GetValue(), \
                self.parent.m_panelPage3.m_ArtisticA.GetValue(), \
                self.parent.m_panelPage3.m_SocialA.GetValue(), \
                self.parent.m_panelPage3.m_EnterprisingA.GetValue(), \
                self.parent.m_panelPage3.m_ConventionalA.GetValue()
                )
        self.axes1.plot(self.x, self.y1, color="blue", marker="o", label="Aktivitas")

# Buat grafik Kompetensi
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y2 = (self.parent.m_panelPage3.m_RealisticK.GetValue(), \
                self.parent.m_panelPage3.m_InvestigativeK.GetValue(), \
                self.parent.m_panelPage3.m_ArtisticK.GetValue(), \
                self.parent.m_panelPage3.m_SocialK.GetValue(), \
                self.parent.m_panelPage3.m_EnterprisingK.GetValue(), \
                self.parent.m_panelPage3.m_ConventionalK.GetValue()
                )
        self.axes1.plot(self.x, self.y2, color="red", marker="o", label="Kompetensi")
# Buat grafik Pekerjaan
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y3 = (self.parent.m_panelPage3.m_RealisticP.GetValue(), \
                self.parent.m_panelPage3.m_InvestigativeP.GetValue(), \
                self.parent.m_panelPage3.m_ArtisticP.GetValue(), \
                self.parent.m_panelPage3.m_SocialP.GetValue(), \
                self.parent.m_panelPage3.m_EnterprisingP.GetValue(), \
                self.parent.m_panelPage3.m_ConventionalP.GetValue()
                )
        self.axes1.plot(self.x, self.y3, color="green", marker="o", label="Pekerjaan")

# Buat grafik Penilaian data diri bagian1                        
                
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y4 = (self.parent.m_panelPage4.m_kmekanisb1.GetValue(), \
                self.parent.m_panelPage4.m_kilmiahb1.GetValue(), \
                self.parent.m_panelPage4.m_kartistikb1.GetValue(), \
                self.parent.m_panelPage4.m_kmengajarb1.GetValue(), \
                self.parent.m_panelPage4.m_kpenjualanb1.GetValue(), \
                self.parent.m_panelPage4.m_kadministrasib1.GetValue()
                )
        self.axes1.plot(self.x, self.y4, color="yellow", marker="o", label="Penilaian Diri Bag 1")

# Buat grafik Penilaian data diri bagian2                    
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y5 = (self.parent.m_panelPage4.m_ktanganb2.GetValue(), \
                self.parent.m_panelPage4.m_kmatematikab2.GetValue(), \
                self.parent.m_panelPage4.m_kmusikb2.GetValue(), \
                self.parent.m_panelPage4.m_moranglainb2.GetValue(), \
                self.parent.m_panelPage4.m_kmanajerialb2.GetValue(), \
                self.parent.m_panelPage4.m_kperkantoranb2.GetValue()
                )
        self.axes1.plot(self.x, self.y5, color="purple", marker="o", label="Penilaian Diri Bag 1")
    
        self.axes1.legend(loc="best")
#         self.axes1.set_ylim(0,20)

        self.figure2 = self.parent.m_panelPage5.m_plota.figure
        self.axes2 = self.figure2.add_subplot(111)
        
#         print ("grafika")
        try:
            for a in range(0, 6):
                self.axes2.lines[0].remove()
        except:
            pass
        
        self.x = ("R", "I", "A", "S", "E", "C")
        self.y6 = (self.parent.sumscoresR, \
                   self.parent.sumscoresI, \
                   self.parent.sumscoresA, \
                   self.parent.sumscoresS, \
                   self.parent.sumscoresE, \
                   self.parent.sumscoresC
                   )
        self.axes2.plot(self.x, self.y6, color="blue", marker="o", label="Summary Scores")
    
        self.axes2.legend(loc="best")

        print ("grafik")
        self.parent.m_panelPage5.m_plota.Fit()
        self.parent.m_panelPage5.m_plota.figure.tight_layout()
        self.parent.m_panelPage5.m_plotb.Fit()
        self.parent.m_panelPage5.m_plotb.figure.tight_layout()
        self.parent.Refresh()
        self.parent.Layout()    
