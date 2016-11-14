__author__ = 'NovikovII'


class BookHelper:

    def __init__(self, app):
        self.app = app

    def add_entry(self, entry):
        wd = self.app.wd
        # open add address book entry
        wd.find_element_by_link_text("add new").click()
        # fill address book entry form
        for key, item in entry.parament.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_entry(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        # select
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def edit_first_entry(self, entry):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        #wd.find_element_by_link_text("add new").click()

        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        for key, item in entry.parament.items():
            wd.find_element_by_name(key).click()
            wd.find_element_by_name(key).clear()
            wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_name("update").click()
        #wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

