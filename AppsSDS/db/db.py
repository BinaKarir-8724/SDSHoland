#!/usr/bin/python
import os
import sqlite3
from shutil import copyfile
import pathlib


def copypastefile(fdata1, fdata2):
    filesumber = fdata1
    filedibuat = fdata2
    src = pathlib.Path.cwd() / filesumber
    dst = pathlib.Path.cwd() / filedibuat
    copyfile(src, dst)
    

def create_connection(db_file):  # db_file):
    try:
        # db_file="db.db"
        conn = sqlite3.connect(db_file)            
        print ("connecting")
        return conn

    except Exception as e:
        print ("file Path is not valid")
        print(e)
        return None

 
def close(conn):
    conn.close()
    print ("Great udah diputus")


def create_table(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)
    return c


def selectdata(conn, create_table_sql):
    c = conn.cursor()
    c.execute(create_table_sql)
    return c

    
def main(db):
    database = db
    sql_create_projects_table = """ 
    CREATE TABLE IF NOT EXISTS `personft` (
    `idpersonft`    int,
    `nama`    text,
    `tgl_tes`    date,
    `jenis_kelamin`    text,
    `tgl_lahir`    date,
    `asal_sekolah`    text,
    `jurusan`    text,
    `kota`    text,
    `hobi`    text,
    `prestasi_akademik`    text,
    `prestasi_non`    akademik text,
    `eksul`    text,
    PRIMARY KEY(`idpersonft`)
);"""

    sql_create_table2 = """
CREATE TABLE IF NOT EXISTS `personfs` (
    `idpersonfs`    int,
    `no_tes`    int,
    `tgl_tes`    date,
    `nama_kandidat`    text,
    `jenis_kelamin`    text,
    `tgl_lahir`    date,
    `pendidikan_terakhir`    text,
    `jurusan`    text,
    `kota`    text,
    `perusahaanorinstansi`    text,
    `posisiorjabatan`    text,
    PRIMARY KEY(`idpersonfs`)
);"""
    sql_create_table3 = """CREATE TABLE IF NOT EXISTS `kuncijawaban`(
                            `idkuncijawaban`    int,
                            `personfsid`    int,
                            `personftid`    int,
                            FOREIGN KEY(`personftid`) REFERENCES `personft`(`idpersonft`),
                            PRIMARY KEY(`idkuncijawaban`),
                            FOREIGN KEY(`personfsid`) REFERENCES `personfs`(`idpersonfs`)
                                ); """
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)
        # create tasks table
       
        create_table(conn, sql_create_table2)
        
        create_table(conn, sql_create_table3)
    else:
        print("Error! cannot create the database connection.")
    
    conn.close()
    print ("sudah ditutup")

    
def createdatabasename(namadatabase, db_file):
 
    print (os.getcwd())
    create_connection(db_file)
    main(namadatabase)


def pathdb():
    
    return pathlib.Path.cwd() / "db/riasec.db"


class QueryList():
    
    def __init__(self):
        
        self.db_file = pathlib.Path.cwd() / "db/riasec.db"
#         self.db_file=pathlib.Path.cwd()/"riasec.db"
#         print (pathlib.Path.cwd()/"db/riasec.db")
        
        pass

    def query(self):
        
        create_connection(self.db_file)
        conn = create_connection(self.db_file)
        
        if conn is not None :
            sql = "SELECT * From fileedit2"
            c = create_table(conn, sql)
            getdata = c.fetchall()
#             print (getdata)
            listboxdata = []
            for row in getdata:
#                 print (row[0])
                print (row)
                listboxdata.append([row[0], row[1], row[2]])
                # listboxdata[row[0]]=row[1]
    #         print (listboxdata)
        else :
            listboxdata = {}
            print("Error! cannot create the database connection.")
        conn.close()
        print ("sudah ditutup")
        print (listboxdata)
        return listboxdata

    def query2(self):
        
        create_connection(self.db_file)
        conn = create_connection(self.db_file)
        
        if conn is not None :
            sql = "SELECT * From fileedit"
            c = create_table(conn, sql)
            getdata = c.fetchall()
#             print (getdata)
            listboxdata = []
            for row in getdata:
#                 print (row[0])
                print (row)
                listboxdata.append([row[0], row[1], row[2]])
                # listboxdata[row[0]]=row[1]
    #         print (listboxdata)
        else :
            listboxdata = {}
            print("Error! cannot create the database connection.")
        conn.close()
        print ("sudah ditutup")
        print (listboxdata)
        return listboxdata
    
    def CheckQuery(self, prof, prof2):
        self.prof = prof
        self.prof2 = prof2
        create_connection(self.db_file)
        conn = create_connection(self.db_file)
        
        if conn is not None :
            sql = "SELECT * From fileedit2 WHERE Profesi = '{}'".format(self.prof)
            c = selectdata(conn, sql)

            getdata = c.fetchall()
#             print (getdata)
            listboxdata = {}
            listboxdata2 = {}
            
            for row in getdata:
                # print (row[0])
                listboxdata[row[0]] = row[1]

            sql2 = "SELECT * From fileedit2 WHERE Code = '{}'".format(self.prof2)            
            c = selectdata(conn, sql2)
            getdata2 = c.fetchall()
                
            for rowa in getdata2:
                listboxdata2[rowa[0]] = rowa[1]
        
        else :
            listboxdata = {}
            listboxdata2 = {}
            print("Error! cannot create the database connection.")
            
        conn.close()
        print ("sudah ditutup")
        
        return listboxdata, listboxdata2   
        
    def CheckQueryedu(self, prof, prof2):
        self.prof = prof
        self.prof2 = prof2
        create_connection(self.db_file)
        conn = create_connection(self.db_file)
        
        if conn is not None :
            sql = "SELECT * From pendidikan WHERE 'Program Studi' = '{}'".format(self.prof)
            c = selectdata(conn, sql)

            getdata = c.fetchall()
#             print (getdata)
            listboxdata = {}
            listboxdata2 = {}
            
            for row in getdata:
                # print (row[0])
                listboxdata[row[0]] = row[1]

            sql2 = "SELECT * From pendidikan WHERE Kode = '{}'".format(self.prof2)            
            c = selectdata(conn, sql2)
            getdata2 = c.fetchall()
                
            for rowa in getdata2:
                listboxdata2[rowa[0]] = rowa[1]
        
        else :
            listboxdata = {}
            listboxdata2 = {}
            print("Error! cannot create the database connection.")
            
        conn.close()
        print ("sudah ditutup")
        
        return listboxdata, listboxdata2           


def Deletedbtes(db_file, row_id):
    print ("Will delete row based on Id number {}".format(row_id))
    db_file = db_file
    conn = create_connection(db_file)
    if conn is not None:
        print ("Conn is connecting now")
        sql = "DELETE FROM databasekandidat2"\
            " WHERE rowid = '{}'".format(row_id)
        selectdata(conn, sql)
        conn.commit()
    else :
        print ("Conn is not connecting")
        
    conn.close()
    

def Deletedb(db_file, row_id):
    print ("Will delete row based on Id number {}".format(row_id))
    db_file = db_file
    conn = create_connection(db_file)
    if conn is not None:
        print ("Conn is connecting now")
        sql = "DELETE FROM databasekandidat1"\
            " WHERE rowid = '{}'".format(row_id)
        selectdata(conn, sql)
        conn.commit()
    else :
        print ("Conn is not connecting")
        
    conn.close()

    
def Updatedbtes(db_file, row_id, *datainput):
    print (datainput)
    print (row_id)
    db_file = db_file
    conn = create_connection(db_file)
    print (row_id)
    if conn is not None :
        print ("Conn is connecting now")
        sql = "UPDATE databasekandidat2"\
              " SET 'Nama' = '{0}','TanggalTes' = '{1}', 'JenisKelamin'='{2}',"\
              "`TanggalLahir`='{3}' , `AsalSekolah`='{4}' , `Jurusan`='{5}' , `AsalUniversitas`='{6}',`Jurusan2`='{7}' , `Kota`='{8}',"\
              " 'Hobi' = '{9}','PrestasiAkademik'='{10}','PrestasiNonAkdemik'='{11}','EkskulYangDiikuti' ='{12}',`OF1` = '{13}', `OF2`='{14}' , `OF3`='{15}',"\
            " `OF4`='{16}' , `OF5`='{17}' , `OF6`='{18}' , `AR`='{19}' , `AI`='{20}' , `AA`='{21}' , `AS`='{22}' , `AE`='{23}' , `AC`='{24}' , `KR`='{25}' ,"\
            " `KI`='{26}' , `KA`='{27}' , `KS`='{28}' , `KE` ='{29}', `KC`='{30}' , `PR`='{31}' , `PI`='{32}' , `PA`='{33}' , `PS` ='{34}', `PE`='{35}' , "\
            " `PC`='{36}' , `PDR`='{37}' , `PDI`='{38}' ,`PDA`='{39}' , `PDS`='{40}' , `PDE` ='{41}', `PDC`='{42}' , `PD2R`='{43}' , `PD2I`='{44}' , `PD2A`='{45}' , "\
            "`PD2S`='{46}' , `PD2E`='{47}' , `PD2C`='{48}' "\
              .format(*datainput) + "where rowid = '{}'".format(row_id)
        selectdata(conn, sql)
        conn.commit()
    
    else :
        print ("Conn is not connecting")

    conn.close()


def Updatedb(db_file, row_id, *datainput):
    print (datainput)
    db_file = db_file
    conn = create_connection(db_file)
    print (row_id)
    if conn is not None :
        print ("Conn is connecting now")
        sql = "UPDATE databasekandidat1"\
              " SET 'NoTes' = '{0}','TanggalTes' = '{1}', 'NamaKandidat' = '{2}', 'JenisKelamin'='{3}',"\
              "`TanggalLahir`='{4}' , `PendidikanTerakhir`='{5}' , `Jurusan`='{6}' , `Kota`='{7}',`Perusahaan/Instansi`='{8}' , `Posisi/Jabatan`='{9}',"\
              " `OF1` = '{10}', `OF2`='{11}' , `OF3`='{12}',"\
            " `OF4`='{13}' , `OF5`='{14}' , `OF6`='{15}' , `AR`='{16}' , `AI`='{17}' , `AA`='{18}' , `AS`='{19}' , `AE`='{20}' , `AC`='{21}' , `KR`='{22}' ,"\
            " `KI`='{23}' , `KA`='{24}' , `KS`='{25}' , `KE` ='{26}', `KC`='{27}' , `PR`='{28}' , `PI`='{29}' , `PA`='{30}' , `PS` ='{31}', `PE`='{32}' , "\
            " `PC`='{33}' , `PDR`='{34}' , `PDI`='{35}' ,`PDA`='{36}' , `PDS`='{37}' , `PDE` ='{38}', `PDC`='{39}' , `PD2R`='{40}' , `PD2I`='{41}' , `PD2A`='{42}' , "\
            "`PD2S`='{43}' , `PD2E`='{44}' , `PD2C`='{45}' "\
              .format(*datainput) + "where rowid = '{}'".format(row_id)
        selectdata(conn, sql)
        conn.commit()
    
    else :
        print ("Conn is not connecting")

    conn.close()
    
    
def Insertdbtes(db_file, *data):
    print (db_file)
    conn = create_connection(db_file)
    if conn is not None :
        print ("conn is not none, ready to insert data into sql")
        sql = "INSERT INTO databasekandidat2(`Nama` , `TanggalTes`,`JenisKelamin`,"\
        "`TanggalLahir` , `AsalSekolah` , `Jurusan` , `AsalUniversitas` , `Jurusan2`, "\
        " `Kota` , `Hobi`,'PrestasiAkademik','PrestasiNonAkdemik','EkskulYangDiikuti' , `OF1` , `OF2` , `OF3`,"\
        " `OF4` , `OF5` , `OF6` , `AR` , `AI` , `AA` , `AS` , `AE` , `AC` , `KR` ,"\
        " `KI` , `KA` , `KS` , `KE` , `KC` , `PR` , `PI` , `PA` , `PS` , `PE` , "\
        " `PC` , `PDR` , `PDI` ,`PDA` , `PDS` , `PDE` , `PDC` , `PD2R` , `PD2I` , `PD2A` , "\
        "`PD2S` , `PD2E` , `PD2C` )"\
        " VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',"\
                 "'{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}',"\
                 "'{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}',"\
                 "'{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}',"\
                 "'{40}','{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}')".format(*data)
        selectdata(conn, sql)
        print ()
        conn.commit()
        
        print (sql)
    else :
        print ("conn is not connecting")
      
    conn.close()
    
    return


def Insertdb(db_file, *data):
#     db_file=pathlib.Path.cwd()/"db/riasec.db"
    print (db_file)
    conn = create_connection(str(db_file))
    if conn is not None :
        print ("conn is not none, ready to insert data into sql")
        sql = "INSERT INTO databasekandidat1(`NoTes` , `TanggalTes`,`NamaKandidat`,"\
        "`JenisKelamin` , `TanggalLahir` , `PendidikanTerakhir` , `Jurusan` , `Kota`, "\
        " `Perusahaan/Instansi` , `Posisi/Jabatan` , `OF1` , `OF2` , `OF3`,"\
        " `OF4` , `OF5` , `OF6` , `AR` , `AI` , `AA` , `AS` , `AE` , `AC` , `KR` ,"\
        " `KI` , `KA` , `KS` , `KE` , `KC` , `PR` , `PI` , `PA` , `PS` , `PE` , "\
        " `PC` , `PDR` , `PDI` ,`PDA` , `PDS` , `PDE` , `PDC` , `PD2R` , `PD2I` , `PD2A` , "\
        "`PD2S` , `PD2E` , `PD2C` )"\
        " VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',"\
                 "'{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}',"\
                 "'{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}',"\
                 "'{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}',"\
                 "'{40}','{41}','{42}','{43}','{44}','{45}')".format(*data)
        selectdata(conn, sql)
        print ()
        conn.commit()
        
        print (sql)
    else :
        print ("conn is not connecting")
      
    conn.close()
    return 


def querydbtes(db_file, nama_orang, date_from, date_end):
  
#     db_file=pathlib.Path.cwd()/"db/riasec.db"
    print(db_file)
    print (nama_orang)
    conn = create_connection(str(db_file))
    if conn is not None :
        print ("conn to databasekandidat2 is not none, is still working")
        
        sql = "SELECT *,rowid FROM databasekandidat2 WHERE Nama = '{}'".format(nama_orang)
        
        sql2 = "SELECT *,rowid FROM databasekandidat2 WHERE TanggalTes  BETWEEN '{}' and '{}'".format(date_from, date_end)

#         sql3  = "SELECT *,rowid FROM databasekandidat2 WHERE NoTes = '{}'".format(no_tes)
        
        c = selectdata(conn, sql)
        getdata = c.fetchall()
        list_data_peserta_tes = []
        
        for rowdata in getdata:
            list_data_peserta_tes.append(rowdata) 
                
        c = selectdata(conn, sql2)
        getdata2 = c.fetchall()
        listdatebydate = []
        for rowdata in getdata2:
            listdatebydate.append(rowdata)

#         c = selectdata(conn,sql3)
#         getdata = c.fetchall()
#         listdatabyno = []
#         
#         for rowdata in getdata:
#             listdatabyno.append(rowdata) 
    else :
        print ("conn is not connecting")
      
    conn.close()
    return list_data_peserta_tes, listdatebydate


def querydb(db_file, nama_orang, date_from, date_end, no_tes):
    
#     db_file=pathlib.Path.cwd()/"db/riasec.db"
    print(db_file)
    conn = create_connection(db_file)
    if conn is not None :
        print ("conn is not none, is still working")
        
        sql = "SELECT *,rowid FROM databasekandidat1 WHERE NamaKandidat = '{}'".format(nama_orang)
        
        sql2 = "SELECT *,rowid FROM databasekandidat1 WHERE TanggalTes  BETWEEN '{}' and '{}'".format(date_from, date_end)

        sql3 = "SELECT *,rowid FROM databasekandidat1 WHERE NoTes = '{}'".format(no_tes)
        
        c = selectdata(conn, sql)
        getdata = c.fetchall()
        listboxdata = []
        
        for rowdata in getdata:
            listboxdata.append(rowdata) 
               
        c = selectdata(conn, sql2)
        getdata2 = c.fetchall()
        listdatebydate = []
        for rowdata in getdata2:
            listdatebydate.append(rowdata)

        c = selectdata(conn, sql3)
        getdata = c.fetchall()
        listdatabyno = []
        
        for rowdata in getdata:
            listdatabyno.append(rowdata) 
    else :
        print ("conn is not connecting")
      
    conn.close()
    return listboxdata, listdatebydate, listdatabyno


def querydbid(db_file, id_row):
    
#     db_file=pathlib.Path.cwd()/"db/riasec.db"
    print(db_file)
    conn = create_connection(db_file)
    if conn is not None :
        print ("conn is not none, is still working")
        
        sql = "SELECT *,rowid FROM databasekandidat1 WHERE rowid = '{}'".format(id_row)
        
        c = selectdata(conn, sql)
        getdata = c.fetchall()
        listboxdata = []
        
        for rowdata in getdata:
            listboxdata.append(rowdata) 
               
        c = selectdata(conn, sql2)
        getdata2 = c.fetchall()
        listdatebydate = []
        for rowdata in getdata2:
            listdatebydate.append(rowdata)

        c = selectdata(conn, sql3)
        getdata = c.fetchall()
        listdatabyno = []
        
        for rowdata in getdata:
            listdatabyno.append(rowdata) 
    else :
        print ("conn is not connecting")
      
    conn.close()
    return listboxdata, listdatebydate, listdatabyno

    
class dataprocess():
    
    def __init___(self):
        
        pass
    
    def __method__(self):
        pass


class CreateDatabaseName():
    
    def __init__(self):
        self.database = []
        self.listfile = os.listdir(os.getcwd())
        print (self.listfile)
    
    def inputnamedatabase(self, adding):
        self.adding = adding
        self.database.append(adding)
        for listf in self.listfile:
            print (listf)
            if listf != self.adding:
                print ("tidak sama")
                self.database.append(listf)
            else :
                print ("data sudah ada")
                break
        return self.database.append(self.adding)

    
if __name__ == '__main__':
#     namadatabase = "riasec"
#     createdatabasename(namadatabase,db_file=None)
#     filesumber = "master.db"
    no_tes = None  # "201672"
    db_file = "riasec.db"
    nama_orang = "Tony Supargo"
    date_from = None  # "1998/01/01"
    date_end = None  # '1998/01/10'
#     copypastefile(filesumber,filedibuat)
#     createdatabasename(filedibuat, db_file=None)
#     file = QueryList()
#     print (file.query())
#     a = "Audiovisual Technician"
#     b = "CSI"
#     x,y = file.CheckQuery(a,None)
#     print (x)
    print (querydb(db_file, nama_orang, date_from, date_end, no_tes))
    dataorang = [   
          "43523534",
          "1998/01/19",
          "FLORDEN INVESTMENTS S.A.",
          "L",
          "1998/01/31",
          "",
          "",
          "BANDUNG",
          "",
          "" ,
          ""  ,
          ""   ,
          ""    ,
          ""   ,
          ""   ,
          ""   ,
          "0"  ,
          "12" ,
          "5"  ,
          "1"  ,
          "9"  ,
          "10" ,
          "7"  ,
          "14" ,
          "5"  ,
          "7"  ,
          "11" ,
          "5"  ,
          "4"  ,
          "7"  ,
          "0"  ,
          "12" ,
          "5"  ,
          "4"  ,
          "4"  ,
          "7"  ,
          "6"  ,
          "6"  ,
          "1"  ,
          "1"  ,
          "4"  ,
          "3"  ,
          "3"  ,
          "4"  ,
          "1"  ,
          "5"  
          ]
      
    Insertdb(db_file, *dataorang)
