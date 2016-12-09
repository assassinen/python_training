__author__ = 'NovikovII'

#import mysql.connector
import pymysql.cursors
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture


#connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()


def load_config():
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json".config.getoption("--target"))
        with open(config_file) as file:
            target = json.load(file)
    return target

db_config = load_config()
#config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
dbfixture = DbFixture(host=db_config['host'], database=db_config['database'], user=db_config['user'], password=db_config['password'])