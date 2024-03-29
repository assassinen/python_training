__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_delele_some_group(app, db, data_groups, chech_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(data_groups)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if chech_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delele_all_group(app, json_groups):
    if app.group.count() == 0:
        app.group.create(json_groups)
    app.group.delete_all_group()
    assert 0 == app.group.count()


