#!/usr/bin/python3
"""A module that list all data in `state` table in `hbtn_0e_0_usa` database
    where name equals a search keyword from the CLI
"""


from sys import argv
import MySQLdb


if __name__ == '__main__':
    dataBaseConnect = MySQLdb.connect(host='localhost',
                                      port=3306, user=argv[1],
                                      passwd=argv[2], db=argv[3],
                                      charset='utf8')
    data = dataBaseConnect.cursor()
    data.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                 .format(argv[4]))
    dataTable = data.fetchall()
    for eachRow in dataTable:
        if eachRow[1] == argv[4]:
            print(eachRow)
    data.close()
    dataBaseConnect.close()
