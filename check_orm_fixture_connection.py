__author__ = 'NovikovII'


from fixture.orm import ORMFixture
from model.group import Group

orm = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    #l = db.get_contact_list()
    #l = db.get_contacts_not_in_group(Group(id="1162"))
    all_groups = orm.get_group_list()
    groups = list(filter(lambda x: len(orm.get_contacts_in_group(x)) > 0, all_groups))
    #for item in l:
    #    print(item)
    print('привет')
    print(all_groups)
    print(groups)
finally:
    pass

