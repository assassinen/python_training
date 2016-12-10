__author__ = 'NovikovII'

#import mysql.connector
import pymysql.cursors



#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    #cursor.execute("select * from group_list")\
    list_contact_fields = ['lastname', 'firstname', 'id', 'address', \
                       'home', 'mobile', 'work', 'fax', 'phone2',  \
                       'email', 'email2', 'email3']
    cursor.execute("select " + ", ".join([i for i in list_contact_fields]) + " from addressbook")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()


