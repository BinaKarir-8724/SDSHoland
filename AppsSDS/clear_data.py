from AppsSDS.simpan_data import SimpanData
from _datetime import datetime


class ClearData(SimpanData):
    
    def __init__(self, parent):
        super(ClearData, self).__init__(parent)
        self.parent.cek_rowid = ""
        self.parent.no_tes_input.SetValue("")
        self.parent.tanggal_tes_input.SetValue(datetime.now())  # datetime.strptime(datetime.now(),'%Y/%m/%d'))
        self.parent.nama_kandidat_input.SetValue("")
        self.parent.jenis_kelamin_input.SetSelection(0)
        self.parent.tanggal_lahir_input.SetValue(datetime.now())  # strptime(datetime.now(),'%Y/%m/%d'))
        self.parent.pendidikan_terakhir_input.SetSelection(0)
        self.parent.jurusan_input.SetValue("")
        self.parent.kota_input.SetValue("")
        self.parent.perusahaan_instansi_input.SetValue("")
        self.parent.posisi_jabatan_input.SetValue("")
        self.parent.nama_input2.SetValue("")
        self.parent.tanggal_tes_input2.SetValue(datetime.now())
        self.parent.jenis_kelamin_input2.SetSelection(0)
        self.parent.tanggal_lahir_input2.SetValue(datetime.now())
        self.parent.asal_sekolah_input2.SetValue("")
        self.parent.jurusan_input21l.SetValue("")
        self.parent.asal_universitas_input2.SetValue("")
        self.parent.jurusan_input2.SetValue("")
        self.parent.kota_input2.SetValue("")
        self.parent.hobi_input2.SetValue("")
        self.parent.prestasi_akademik_input2.SetValue("")
        self.parent.prestasi_non_akademik_input2.SetValue("")
        self.parent.ekskul_yang_diikuti_input2.SetValue("")
        print ("nilai {}".format(self.parent.cek_rowid))
        
        self.listcontrol = [
        self.parent.m_panelPage2.textctrl1,
        self.parent.m_panelPage2.textctrl2,
        self.parent.m_panelPage2.textctrl3,
        self.parent.m_panelPage2.textctrl4,
        self.parent.m_panelPage2.textctrl5,
        self.parent.m_panelPage2.textctrl6,
        self.parent.m_panelPage3.m_RealisticA,
        self.parent.m_panelPage3.m_InvestigativeA,
        self.parent.m_panelPage3.m_ArtisticA,
        self.parent.m_panelPage3.m_SocialA,
        self.parent.m_panelPage3.m_EnterprisingA,
        self.parent.m_panelPage3.m_ConventionalA,
        self.parent.m_panelPage3.m_RealisticK,
        self.parent.m_panelPage3.m_InvestigativeK,
        self.parent.m_panelPage3.m_ArtisticK,
        self.parent.m_panelPage3.m_SocialK,
        self.parent.m_panelPage3.m_EnterprisingK,
        self.parent.m_panelPage3.m_ConventionalK,
        self.parent.m_panelPage3.m_RealisticP,
        self.parent.m_panelPage3.m_InvestigativeP,
        self.parent.m_panelPage3.m_ArtisticP,
        self.parent.m_panelPage3.m_SocialP,
        self.parent.m_panelPage3.m_EnterprisingP,
        self.parent.m_panelPage3.m_ConventionalP ,
        self.parent.m_panelPage4.m_kmekanisb1,
        self.parent.m_panelPage4.m_kilmiahb1,
        self.parent.m_panelPage4.m_kartistikb1,
        self.parent.m_panelPage4.m_kmengajarb1,
        self.parent.m_panelPage4.m_kpenjualanb1,
        self.parent.m_panelPage4.m_kadministrasib1,
        self.parent.m_panelPage4.m_ktanganb2,
        self.parent.m_panelPage4.m_kmatematikab2,
        self.parent.m_panelPage4.m_kmusikb2,
        self.parent.m_panelPage4.m_moranglainb2,
        self.parent.m_panelPage4.m_kmanajerialb2,
        self.parent.m_panelPage4.m_kperkantoranb2
        ]    
        for clear in self.listcontrol :
            clear.SetValue("")
#             print (clear.GetValue())
        print ("lewat sini")
        
        self.parent.m_tombolHitungOnButtonClick(self)
        
    def clear_alldatas(self):
        
        pass


if __name__ == '__main__':
    ClearData()
