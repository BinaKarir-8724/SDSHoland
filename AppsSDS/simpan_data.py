from AppsSDS.db.db import Insertdb, Updatedb, Insertdbtes, Updatedbtes
from AppsSDS.datatersimpan import FrameSimpanSukses


class SimpanData():
    
    def __init__(self, parent):
        
        print ("This is the class to save your input data")
        self.parent = parent
        self.db_file = self.parent.db_file
        
        if self.parent.m_radioBtn1.GetValue() == True :
    #         Format Input Form Seleksi
            self.listdatapribadi = [ 
            self.parent.no_tes_input.GetValue(),
            self.parent.tanggal_tes_input.GetValue().Format("%Y/%m/%d"),
            self.parent.nama_kandidat_input.GetValue(),
            self.parent.jenis_kelamin_input.GetString(self.parent.jenis_kelamin_input.GetSelection()),
            self.parent.tanggal_lahir_input.GetValue().Format("%Y/%m/%d"),
            self.parent.pendidikan_terakhir_input.GetString(\
            self.parent.pendidikan_terakhir_input.GetSelection()),
            self.parent.jurusan_input.GetValue(),
            self.parent.kota_input.GetValue(),
            self.parent.perusahaan_instansi_input.GetValue(),
            self.parent.posisi_jabatan_input.GetValue(),
            ]
            self.rdbtnaktiv = 1 
            
        elif self.parent.m_radioBtn2.GetValue() == True :
    #         Format Input Form Tes
            self.listdatapribadi = [
            self.parent.nama_input2.GetValue(),
            self.parent.tanggal_tes_input2.GetValue().Format("%Y/%m/%d"),
            self.parent.jenis_kelamin_input2.GetString(self.parent.jenis_kelamin_input2.GetSelection()),
            self.parent.tanggal_lahir_input2.GetValue().Format("%Y/%m/%d"),
            self.parent.asal_sekolah_input2.GetValue(),
            self.parent.jurusan_input21l.GetValue(),
            self.parent.asal_universitas_input2.GetValue(),
            self.parent.jurusan_input2.GetValue(),
            self.parent.kota_input2.GetValue(),
            self.parent.hobi_input2.GetValue(),
            self.parent.prestasi_akademik_input2.GetValue(),
            self.parent.prestasi_non_akademik_input2.GetValue(),
            self.parent.ekskul_yang_diikuti_input2.GetValue(),
            ]
            self.rdbtnaktiv = 2
        
        self.lista = [
            self.parent.m_panelPage2.textctrl1.GetValue(),
            self.parent.m_panelPage2.textctrl2.GetValue(),
            self.parent.m_panelPage2.textctrl3.GetValue(),
            self.parent.m_panelPage2.textctrl4.GetValue(),
            self.parent.m_panelPage2.textctrl5.GetValue(),
            self.parent.m_panelPage2.textctrl6.GetValue(),
            self.parent.nilai_RealisticA,
            self.parent.nilai_InvestigativeA ,
            self.parent.nilai_ArtisticA      ,
            self.parent.nilai_SocialA        ,
            self.parent.nilai_EnterprisingA  ,
            self.parent.nilai_ConventionalA  ,
            self.parent.nilai_RealisticK     ,
            self.parent.nilai_InvestigativeK ,
            self.parent.nilai_ArtisticK   ,
            self.parent.nilai_SocialK      ,
            self.parent.nilai_EnterprisingK ,
            self.parent.nilai_ConventionalK  ,
            self.parent.nilai_RealisticP     ,
            self.parent.nilai_InvestigativeP ,
            self.parent.nilai_ArtisticP      ,
            self.parent.nilai_SocialP        ,
            self.parent.nilai_EnterprisingP  ,
            self.parent.nilai_ConventionalP  ,
            self.parent.nilai_Kmekanisb1    ,
            self.parent.nilai_Kilmiahb1     ,
            self.parent.nilai_Kartistikb1    ,
            self.parent.nilai_Kmengajarb1    ,
            self.parent.nilai_Kpenjualan     ,
            self.parent.nilai_Kadministrasib1 ,
            self.parent.nilai_Ktanganb2      ,
            self.parent.nilai_Kmatematikab2  ,
            self.parent.nilai_Kmusikb2      ,
            self.parent.nilai_Moranglain     ,
            self.parent.nilai_Kmanajerial     ,
            self.parent.nilai_Kperkantoran    ,
            ]
    
    def simpan_data(self):
        if self.rdbtnaktiv == 1 :
            print ("Save your Selection Form")
            
            self.data = self.listdatapribadi + self.lista
            print (self.parent.nilai_Kperkantoran)
            print (self.listdatapribadi)
            print (self.lista)
            
            print ("cek row id")
            print (self.data)
            print (self.parent.cek_rowiddata())
            
            if self.parent.cek_rowiddata() == "":
                Insertdb(self.db_file, *self.data)
            else :
                Updatedb(self.db_file, self.parent.cek_rowiddata(), *self.data)            
            
        if self.rdbtnaktiv == 2 :
            print ("Save your Tes Form")
            self.data = self.listdatapribadi + self.lista
            print (self.parent.cek_rowiddata())
            if self.parent.cek_rowiddata() == "":
                Insertdbtes(self.db_file, *self.data)
            else :
                Updatedbtes(self.db_file, self.parent.cek_rowiddata(), *self.data)            
            
            pass
        
        self.datatersimpan = FrameSimpanSukses(self.parent)
        self.datatersimpan.Show()
        
    
