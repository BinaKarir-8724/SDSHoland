
import sqlite3
import pathlib
import os


def query():
    path_of_database = pathlib.Path.cwd() / "db/riasec.db"
    print (path_of_database)
    connect = sqlite3.connect(path_of_database)
   
    cursor = connect.cursor()
    sql = """
    SELECT * FROM 'fileedit'
    """
    cursor.execute(sql)
    data = []
    datas = cursor.fetchall()

    for x in datas:
        data.append(x)
    # print (data)
    connect.close()

    return data


def goapps(queryname):

    # startconnection()
    data = query()
    # finish = "Y"
    # print (data)
    # carinama = input("Cari nama disini\n")
    carinama = queryname
    y = len(carinama)
    data_search = []
    # data_search = {}

    # print (len(data))

    # print (data[1][1])
    for x in range(len(data)):
        if carinama.upper() == data[x][2][0:y].upper(): 
            # print (data[x][0])
            # data_search[data[x][0]]=data[x][1]
            data_search.append([data[x][0], data[x][1], data[x][2]])
    return data_search


def goapps_kode(queryname):

    # startconnection()
    data = query()
    # finish = "Y"
    # print (data)
    # carinama = input("Cari nama disini\n")
    carinama = queryname
    y = len(carinama)
    data_search = []
    # data_search = {}

    # print (len(data))

    # print (data[1][1])
    for x in range(len(data)):
        if carinama.upper() == data[x][0][0:y].upper(): 
            # print (data[x][0])
            # data_search[data[x][0]]=data[x][1]
            data_search.append([data[x][0], data[x][1], data[x][2]])
    return data_search


if __name__ == "__main__":
    os.chdir("..")
    print (goapps(queryname))
    pass
