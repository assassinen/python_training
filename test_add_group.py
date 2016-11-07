# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from group import Group
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class problem_test(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_problem_test(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="test", header="test", footer="test"))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
