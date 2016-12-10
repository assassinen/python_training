__author__ = 'NovikovII'

import mysql.connector
#import pymysql.cursors

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection.autocommit = True

try:
    list=[]
    cursor = connection.cursor()
    list_contact_fields = ['lastname', 'firstname', 'id', 'address', \
                       'home', 'mobile', 'work', 'fax', 'phone2',  \
                       'email', 'email2', 'email3']
    cursor.execute("select " + ", ".join([i for i in list_contact_fields]) + \
                   " from addressbook where deprecated='0000-00-00 00:00:00'")
                    #deprecated is Null")
    for row in cursor:
        dict_contact_fields = {}
        for i in range(len(row)):
            dict_contact_fields[list_contact_fields[i]] = row[i]
        list.append(dict_contact_fields)
    for i in list:
        print(i)
finally:
    connection.close()


