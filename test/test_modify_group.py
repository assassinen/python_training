__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_modify_group_name(app, db, data_groups, chech_ui):
    if app.group.count() == 0:
        app.group.create(data_groups)
    old_groups = db.get_group_list()

    group = random.choice(old_groups)
    old_groups.remove(group)
    mod_group = Group(name="modify_name")
    mod_group.id = group.id
    old_groups.append(mod_group)

    app.group.modify_group_by_id(group.id, mod_group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if chech_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
