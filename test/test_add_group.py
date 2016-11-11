__author__ = 'NovikovII'

# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test", header="test", footer="test"))
    app.group.create(Group(name="test1", header="test1", footer="test1"))

