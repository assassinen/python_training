__author__ = 'NovikovII'
from model.group import Group
from model.contact import Contact
import mysql.connector



class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=database, user=user, password=password)
        #self.connection = pymysql.connect(host=host, database=database, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, \
                            group_name, \
                            group_header, \
                            group_footer \
                            from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            list_contact_fields = ['lastname', 'firstname', 'id', 'address', \
                           'home', 'mobile', 'work', 'fax', 'phone2',  \
                           'email', 'email2', 'email3']
            cursor.execute("select " + ", ".join([i for i in list_contact_fields]) + \
                            " from addressbook where deprecated='0000-00-00 00:00:00'")
                                    #deprecated is Null" тоже работает...
            for row in cursor:
                dict_contact_fields = {}
                for i in range(len(row)):
                    dict_contact_fields[list_contact_fields[i]] = row[i]
                list.append(Contact(**dict_contact_fields))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()