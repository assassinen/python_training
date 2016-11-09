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
