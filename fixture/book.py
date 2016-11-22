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
        self.entry_cache = None

    def delete_first_entry(self):
        self.delete_entry_by_index(0)

    def delete_entry_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.entry_cache = None

    def edit_first_entry(self, entry):
        self.edit_entry_by_index(0, entry)

    def edit_entry_by_index(self, index, entry):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr["+str(index+2)+"]/td[8]/a/img").click()
        for key, item in entry.parament.items():
            if key != 'id':
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_name("update").click()
        self.entry_cache = None


    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    entry_cache = None

    def get_entry_list(self):
        if self.entry_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.entry_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.entry_cache.append(BookEntry(lastname=lastname, firstname=firstname, id=id))
        return list(self.entry_cache)