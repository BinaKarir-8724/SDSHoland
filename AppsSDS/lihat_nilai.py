import wx
from AppsSDS.halaman import Halaman6


class LihatNilai():
    
    def __init__(self, parent):  
        print ("You have choose Lihat Nilai")
        self.lihat_nilai = parent
        try :
            
            self.item = self.lihat_nilai.datpes.m_ListDataPeserta.GetFocusedItem()
            self.item = self.lihat_nilai.datpes.m_ListDataPeserta.GetItem(self.item, 3).GetText()
            from AppsSDS.db import db
                 
            self.db_file = str(db.pathdb())
            self.nama_orang = self.item
            self.date_from = None
            self.date_end = None
            self.no_tes = None
            
            self.querydb = db.querydb(self.db_file, self.nama_orang, self.date_from, self.date_end, self.no_tes)[0][0]
            
            print (self.querydb)
            
            for i in self.querydb:
                print (i)
            print (self.item)    
        
        except:
            pass
        
        try :
            print ("hello apa kabar")
            self.item = self.lihat_nilai.buka_peserta_tes.m_ListDataPeserta.GetFocusedItem()
            self.item = self.lihat_nilai.buka_peserta_tes.m_ListDataPeserta.GetItem(self.item, 1).GetText()
            from AppsSDS.db import db
                 
            self.db_file = str(db.pathdb())
            self.nama_orang = self.item
            self.date_from = None
            self.date_end = None
            self.no_tes = None
            
            self.querydb = db.querydbtes(self.db_file, self.nama_orang, self.date_from, self.date_end)[0][0]
            
            print (self.querydb)
            
            for i in self.querydb:
                print (i)
            print (self.item)               
            
        except:
            pass
     
    def insert_value(self):    
        from datetime import datetime
        try :
            self.lihat_nilai.no_tes_input.SetValue(self.querydb[0])
            self.lihat_nilai.tanggal_tes_input.SetValue(datetime.strptime(self.querydb[1], '%Y/%m/%d'))
            self.lihat_nilai.nama_kandidat_input.SetValue(self.querydb[2])
            if self.querydb[3] == "Laki-Laki":
                self.n = 0
            elif self.querydb[3] == "Perempuan" :
                self.n = 1
            else :
                self.n = 0
             
            self.lihat_nilai.jenis_kelamin_input.SetSelection(self.n)
            self.lihat_nilai.tanggal_lahir_input.SetValue(datetime.strptime(self.querydb[4], '%Y/%m/%d'))
             
            if self.querydb[5] == "SD" :
                self.n = 0
            elif self.querydb[5] == "SMP":
                self.lihat_nilai.n = 1
            elif self.querydb[5] == "SMA/Sederajat":
                self.n = 2
            elif self.querydb[5] == "S1":
                self.n = 3
            elif self.querydb[5] == "S2":
                self.n = 4
            elif self.querydb[5] == "S3":
                self.n = 4
            else :
                self.n = 0
            self.lihat_nilai.pendidikan_terakhir_input.SetSelection(self.n)
            self.lihat_nilai.jurusan_input.SetValue(self.querydb[6])
            self.lihat_nilai.kota_input.SetValue(self.querydb[7])
            self.lihat_nilai.perusahaan_instansi_input.SetValue(self.querydb[8])
            self.lihat_nilai.posisi_jabatan_input.SetValue(self.querydb[9])

        except:
            pass
        
        try :
            print (self.lihat_nilai.nama_input2.SetValue(self.querydb[0]))
            
            pass
        
        except :
            
            pass
 
        from AppsSDS.db.db import QueryList
        
        try :
            self.querylist = QueryList()
            self.lihat_nilai.m_panelPage2.textctrl1.SetValue(self.querydb[10])
            self.lihat_nilai.m_panelPage2.textctrl2.SetValue(self.querydb[11])
            self.lihat_nilai.m_panelPage2.textctrl3.SetValue(self.querydb[12])
            self.lihat_nilai.m_panelPage2.textctrl4.SetValue(self.querydb[13])
            self.lihat_nilai.m_panelPage2.textctrl5.SetValue(self.querydb[14])
            self.lihat_nilai.m_panelPage2.textctrl6.SetValue(self.querydb[15])
        
            self.lihat_nilai.m_panelPage3.m_RealisticA.SetValue(self.querydb[16])
            self.lihat_nilai.m_panelPage3.m_InvestigativeA.SetValue(self.querydb[17])
            self.lihat_nilai.m_panelPage3.m_ArtisticA.SetValue(self.querydb[18])
            self.lihat_nilai.m_panelPage3.m_SocialA.SetValue(self.querydb[19])
            self.lihat_nilai.m_panelPage3.m_EnterprisingA.SetValue(self.querydb[20])
            self.lihat_nilai.m_panelPage3.m_ConventionalA.SetValue(self.querydb[21])
            
            self.lihat_nilai.m_panelPage3.m_RealisticK.SetValue(self.querydb[22])
            self.lihat_nilai.m_panelPage3.m_InvestigativeK.SetValue(self.querydb[23])
            self.lihat_nilai.m_panelPage3.m_ArtisticK.SetValue(self.querydb[24])
            self.lihat_nilai.m_panelPage3.m_SocialK.SetValue(self.querydb[25])
            self.lihat_nilai.m_panelPage3.m_EnterprisingK.SetValue(self.querydb[26])
            self.lihat_nilai.m_panelPage3.m_ConventionalK.SetValue(self.querydb[27])
            
            self.lihat_nilai.m_panelPage3.m_RealisticP.SetValue(self.querydb[28])
            self.lihat_nilai.m_panelPage3.m_InvestigativeP.SetValue(self.querydb[29])
            self.lihat_nilai.m_panelPage3.m_ArtisticP.SetValue(self.querydb[30])
            self.lihat_nilai.m_panelPage3.m_SocialP.SetValue(self.querydb[31])
            self.lihat_nilai.m_panelPage3.m_EnterprisingP.SetValue(self.querydb[32])
            self.lihat_nilai.m_panelPage3.m_ConventionalP.SetValue(self.querydb[33])
            
            self.lihat_nilai.m_panelPage4.m_kmekanisb1.SetValue(self.querydb[34])
            self.lihat_nilai.m_panelPage4.m_kilmiahb1.SetValue(self.querydb[35])
            self.lihat_nilai.m_panelPage4.m_kartistikb1.SetValue(self.querydb[36])
            self.lihat_nilai.m_panelPage4.m_kmengajarb1.SetValue(self.querydb[37])
            self.lihat_nilai.m_panelPage4.m_kpenjualanb1.SetValue(self.querydb[38])
            self.lihat_nilai.m_panelPage4.m_kadministrasib1.SetValue(self.querydb[39])
                    
            self.lihat_nilai.m_panelPage4.m_ktanganb2.SetValue(self.querydb[40])
            self.lihat_nilai.m_panelPage4.m_kmatematikab2.SetValue(self.querydb[41])
            self.lihat_nilai.m_panelPage4.m_kmusikb2.SetValue(self.querydb[42])
            self.lihat_nilai.m_panelPage4.m_moranglainb2.SetValue(self.querydb[43])
            self.lihat_nilai.m_panelPage4.m_kmanajerialb2.SetValue(self.querydb[44])
            self.lihat_nilai.m_panelPage4.m_kperkantoranb2.SetValue(self.querydb[45])
            
            self.lihat_nilai.datpes.Close()
    
            self.lihat_nilai.m_button1.Enable()
            self.lihat_nilai.m_button3.Enable()     
            self.lihat_nilai.m_button2.Enable()
       
            self.lihat_nilai.m_panel9.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.m_panel1.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.panel_radiobtn_halaman1.Hide()
            self.lihat_nilai.halaman1.Hide()
            self.lihat_nilai.halaman2.Hide()
            self.lihat_nilai.halaman3.Hide()
            self.lihat_nilai.halaman6.Hide()
            self.lihat_nilai.halaman7.Hide()

    
            self.lihat_nilai.halaman4.Show()
            
            self.lihat_nilai.btn_selanjutnya(self)
            print ("sdds")
            self.lihat_nilai.m_tombolHitungOnButtonClick(self.lihat_nilai)
            print ("sdds")
        except :
            print("kesini")
            pass
        
        try:
            print ("tes")
            
        except :
            pass
        
    def cek_rowid(self):
        return self.querydb[46]
    

class LihatNilaiTes():
    
    def __init__(self, parent):  
        print ("You have choose Lihat Nilai")
        try :
            self.lihat_nilai = parent

            print ("hello apa kabar")
            self.item = self.lihat_nilai.buka_peserta_tes.m_ListDataPeserta.GetFocusedItem()
            self.item = self.lihat_nilai.buka_peserta_tes.m_ListDataPeserta.GetItem(self.item, 1).GetText()
            from AppsSDS.db import db
                
            self.db_file = str(db.pathdb())
            self.nama_orang = self.item
            self.date_from = None
            self.date_end = None
            self.no_tes = None
            
            self.querydb = db.querydbtes(self.db_file, self.nama_orang, self.date_from, self.date_end)[0][0]
            
            print (self.querydb)
            
            for i in self.querydb:
                print (i)
            print (self.item)               
        except:
            pass

    def insert_value(self):    
        from datetime import datetime
  
        print (self.lihat_nilai.nama_input2.SetValue(self.querydb[0]))
        self.lihat_nilai.tanggal_tes_input2.SetValue(datetime.strptime(self.querydb[1], '%Y/%m/%d'))
        if self.querydb[2] == "Laki-Laki":
            self.n = 0
        elif self.querydb[2] == "Perempuan" :
            self.n = 1
        else :
            self.n = 0
            
        self.lihat_nilai.jenis_kelamin_input2.SetSelection(self.n)
        self.lihat_nilai.tanggal_lahir_input2.SetValue(datetime.strptime(self.querydb[3], '%Y/%m/%d'))
        self.lihat_nilai.asal_sekolah_input2.SetValue(self.querydb[4])
        self.lihat_nilai.jurusan_input21l.SetValue(self.querydb[5])
        self.lihat_nilai.asal_universitas_input2.SetValue(self.querydb[6])
        self.lihat_nilai.jurusan_input2.SetValue(self.querydb[7])
        self.lihat_nilai.kota_input2.SetValue(self.querydb[8])
        self.lihat_nilai.hobi_input2.SetValue(self.querydb[9])
        self.lihat_nilai.prestasi_akademik_input2.SetValue(self.querydb[10])
        self.lihat_nilai.prestasi_non_akademik_input2.SetValue(self.querydb[11])
        self.lihat_nilai.ekskul_yang_diikuti_input2.SetValue(self.querydb[12])


        from AppsSDS.db.db import QueryList
        try :
            self.querylist = QueryList()
            self.lihat_nilai.m_panelPage2.textctrl1.SetValue(self.querydb[13])
            self.lihat_nilai.m_panelPage2.textctrl2.SetValue(self.querydb[14])
            self.lihat_nilai.m_panelPage2.textctrl3.SetValue(self.querydb[15])
            self.lihat_nilai.m_panelPage2.textctrl4.SetValue(self.querydb[16])
            self.lihat_nilai.m_panelPage2.textctrl5.SetValue(self.querydb[17])
            self.lihat_nilai.m_panelPage2.textctrl6.SetValue(self.querydb[18])
        
            self.lihat_nilai.m_panelPage3.m_RealisticA.SetValue(self.querydb[19])
            self.lihat_nilai.m_panelPage3.m_InvestigativeA.SetValue(self.querydb[20])
            self.lihat_nilai.m_panelPage3.m_ArtisticA.SetValue(self.querydb[21])
            self.lihat_nilai.m_panelPage3.m_SocialA.SetValue(self.querydb[22])
            self.lihat_nilai.m_panelPage3.m_EnterprisingA.SetValue(self.querydb[23])
            self.lihat_nilai.m_panelPage3.m_ConventionalA.SetValue(self.querydb[24])
            
            self.lihat_nilai.m_panelPage3.m_RealisticK.SetValue(self.querydb[25])
            self.lihat_nilai.m_panelPage3.m_InvestigativeK.SetValue(self.querydb[26])
            self.lihat_nilai.m_panelPage3.m_ArtisticK.SetValue(self.querydb[27])
            self.lihat_nilai.m_panelPage3.m_SocialK.SetValue(self.querydb[28])
            self.lihat_nilai.m_panelPage3.m_EnterprisingK.SetValue(self.querydb[29])
            self.lihat_nilai.m_panelPage3.m_ConventionalK.SetValue(self.querydb[30])
            
            self.lihat_nilai.m_panelPage3.m_RealisticP.SetValue(self.querydb[31])
            self.lihat_nilai.m_panelPage3.m_InvestigativeP.SetValue(self.querydb[32])
            self.lihat_nilai.m_panelPage3.m_ArtisticP.SetValue(self.querydb[33])
            self.lihat_nilai.m_panelPage3.m_SocialP.SetValue(self.querydb[34])
            self.lihat_nilai.m_panelPage3.m_EnterprisingP.SetValue(self.querydb[35])
            self.lihat_nilai.m_panelPage3.m_ConventionalP.SetValue(self.querydb[36])
            
            self.lihat_nilai.m_panelPage4.m_kmekanisb1.SetValue(self.querydb[37])
            self.lihat_nilai.m_panelPage4.m_kilmiahb1.SetValue(self.querydb[38])
            self.lihat_nilai.m_panelPage4.m_kartistikb1.SetValue(self.querydb[39])
            self.lihat_nilai.m_panelPage4.m_kmengajarb1.SetValue(self.querydb[40])
            self.lihat_nilai.m_panelPage4.m_kpenjualanb1.SetValue(self.querydb[41])
            self.lihat_nilai.m_panelPage4.m_kadministrasib1.SetValue(self.querydb[42])
                    
            self.lihat_nilai.m_panelPage4.m_ktanganb2.SetValue(self.querydb[43])
            self.lihat_nilai.m_panelPage4.m_kmatematikab2.SetValue(self.querydb[44])
            self.lihat_nilai.m_panelPage4.m_kmusikb2.SetValue(self.querydb[45])
            self.lihat_nilai.m_panelPage4.m_moranglainb2.SetValue(self.querydb[46])
            self.lihat_nilai.m_panelPage4.m_kmanajerialb2.SetValue(self.querydb[47])
            self.lihat_nilai.m_panelPage4.m_kperkantoranb2.SetValue(self.querydb[48])
            
            self.lihat_nilai.buka_peserta_tes.Close()
    
            self.lihat_nilai.m_button1.Enable()
            self.lihat_nilai.m_button3.Enable()     
            self.lihat_nilai.m_button2.Enable()
       
            self.lihat_nilai.m_panel9.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.m_panel1.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.SetBackgroundColour(wx.Colour(91, 85, 112))
            self.lihat_nilai.panel_radiobtn_halaman1.Hide()
            self.lihat_nilai.halaman1.Hide()
            self.lihat_nilai.halaman2.Hide()
            self.lihat_nilai.halaman3.Hide()
            self.lihat_nilai.halaman6.Hide()
            self.lihat_nilai.halaman7.Hide()
    
            self.lihat_nilai.halaman4.Show()
            
            self.lihat_nilai.btn_selanjutnya(self)
            print ("sdds")
            self.lihat_nilai.m_tombolHitungOnButtonClick(self.lihat_nilai)
        except :
            pass
       
    def cek_rowidtes(self):
        return self.querydb[49]
