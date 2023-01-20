#!/usr/bin/python3
"""A module that list all data in `state` table in `hbtn_0e_0_usa` database
    with name starting with 'N'
 """


from sys import argv
import MySQLdb


if __name__ == '__main__':
    dataBaseConnect = MySQLdb.connect(host='localhost',
                                      port=3306, user=argv[1],
                                      passwd=argv[2], db=argv[3],
                                      charset='utf8')
    data = dataBaseConnect.cursor()
    data.execute("SELECT cities.name FROM cities WHERE cities.state_id = \
                (SELECT state.id FROM states WHERE states.name = '{}' \
                 LIMIT 1) ORDER BY cities.id ASC".format(argv[4]))
    dataTable = data.fetchall()
    newData = []
    for eachRow in dataTable:
        newData.append(eachRow[0])
    print(", ".join(newData))
    data.close()
    dataBaseConnect.close()
