# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from book_entry import BookEntry
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_entry(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_test_add_entry(self):
        self.app.login(username="admin", password="secret")
        addEntry = BookEntry(firstname="Светлана", middlename="Иларионовна", lastname="Смирнова", work="безработный", address="Не дом и не улица", mobile='8915223344')
        self.app.add_book_entry(addEntry)
        self.app.logout()
    
    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
