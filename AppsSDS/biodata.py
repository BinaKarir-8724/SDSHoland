'''
Created on Jan 4, 2019

@author: binakarir
'''


class Pilih(object):
  
#         biodata = [self.m_radioBtn1,self.m_radioBtn2]
# 1        biodata_peserta = [ self.no_tes_input,
# 2                            self.tanggal_tes_input,
# 3                            self.nama_kandidat_input,
# 4                            self.jenis_kelamin_input,
# 5                            self.tanggal_lahir_input,
# 6                            self.pendidikan_terakhir_input,
# 7                            self.jurusan_input,
# 8                            self.kota_input,
# 9                            self.perusahaan_instansi_input,
# 10                            self.posisi_jabatan_input,
# 11                            self.no_tes_input2,
# 12                            self.tanggal_tes_input2,
# 13                            self.jenis_kelamin_input2,
# 14                            self.tanggal_lahir_input2,
# 15                            self.asal_sekolah_input2,
#                             self.jurusan_input2,
#                             self.asal_universitas_input2,
#                             self.jurusan_input21,
#                             self.asal_sekolah_input2,
#                             self.kota_input2,
#                             self.hobi_input2,
#                             self.prestasi_akademik_input2,
#                             self.prestasi_non_akademik_input2,
#                             self.ekskul_yang_diikuti_input2,
#         ]
    
    def __init__(self, *args):
        self.biodata = args
        self.listbiodata = []
#         self.input_data_no = self.input_data[0]
#         self.m_radioBtn1= self.radio_button[0]
#         self.m_radioBtn2= self.radio_button[1]
# #         self.m_radioBtn2=args[1]
#         print (self.m_radioBtn1.GetValue())
#         print (self.m_radioBtn2.GetValue())

        if self.biodata[0][0].GetValue() == True:
            print ("Form Seleksi")
#             self.no_tes_input.SetValue("ajalksdf")
            for i in range(0, 10):
                try:
                    print (self.biodata[1][i].GetValue())
                    self.a = self.biodata[1][i].GetValue()
                    self.listbiodata.append(self.a)
                except:
                    print (self.biodata[1][i].GetString(self.biodata[1][3].GetSelection()))
                    self.a = self.biodata[1][i].GetString(self.biodata[1][3].GetSelection())
                    self.listbiodata.append(self.a)

        elif self.biodata[0][1].GetValue() == True :
            print ("Form Tes")
            print (self.biodata[1][0].GetValue())
            
        print (self.listbiodata)

    def getdata(self):
        
        return self.a, self.b, self.c
