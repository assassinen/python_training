__author__ = 'NovikovII'

from model.book import BookEntry

class BookHelper:

    def __init__(self, app):
        self.app = app

    def add_entry(self, entry):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        for key, item in entry.parament.items():
            if key != 'id':
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_entry(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def edit_first_entry(self, entry):
        wd = self.app.wd
        self.open_home_page()

        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        for key, item in entry.parament.items():
            if key != 'id':
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_name("update").click()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_entry_list(self):
        wd = self.app.wd
        self.open_home_page()
        entry = []
        for element in wd.find_elements_by_name("entry"):
            lastname = element.find_elements_by_tag_name("td")[1].text
            firstname = element.find_elements_by_tag_name("td")[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            entry.append(BookEntry(lastname=lastname, firstname=firstname, id=id))
        return entry