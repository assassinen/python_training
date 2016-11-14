__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_modify_group_name(app):
    app.group.modify(Group(name="modify_name"))

def test_modify_group_header(app):
    app.group.modify(Group(header="modify_header"))
