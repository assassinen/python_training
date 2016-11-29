__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_empty_group(app):
    testdata = []
    for i in range(1, 6):
        testdata.append(Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i)))
    for group in testdata:
        old_groups = app.group.get_group_list()
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        old_groups.append(group)
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

