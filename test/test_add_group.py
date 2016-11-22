__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    for i in range (1, 6):
        group = Group(name="test"+str(i), header="test"+str(i), footer="test"+str(i))
        app.group.create(group)
        assert len(old_groups) + 1 == app.group.count()
        old_groups.append(group)
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="test", header="test", footer="test")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

