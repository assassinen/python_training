__author__ = 'NovikovII'

from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_contact(self, entry):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        for key, item in entry.paramentr.items():
            if key != 'id':
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_first_contact(self, entry):
        self.edit_contact_by_index(0, entry)

    def edit_contact_by_index(self, index, entry):
        wd = self.app.wd
        self.open_home_page()
        self.open_contact_to_edit_by_index(index)
        for key, item in entry.paramentr.items():
            if key != 'id':
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(item)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/"):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = cells[3].text
                all_email = cells[4].text
                all_phone = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id, address=address, all_phone_from_home_page = all_phone, all_emal_from_home_page = all_email))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    list_contact_fields = ['lastname', 'firstname', 'id', 'address', \
                           'home', 'mobile', 'work', 'fax', 'phone2',  \
                           'email', 'email2', 'email3']

    def get_contact_list_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        dict_contact_fields = {}
        for field in self.list_contact_fields:
            dict_contact_fields[field] = wd.find_element_by_name(field).get_attribute("value")
        return Contact(**dict_contact_fields)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        mobile = re.search("M: (.*)", text).group(1)
        return Contact(mobile=mobile)

