__author__ = 'NovikovII'

from sys import maxsize
import sys
import os

class Contact:
    def __init__(self):
        pass
        # self.parament = {'id': None, 'lastname': None, 'firstname': None}
        # for key, item in kwargs.items():
        #     self.parament[key] = item

        self.parament = ['firstname', 'lastname']
        for i in self.parament:
            eval('self.'+i)



    # def __repr__(self):
    #     return "%s: %s %s" % (self.parament['id'], self.parament['lastname'],  self.parament['firstname'])
    #
    # def __eq__(self, other):
    #     return (self.parament['id'] is None or other.parament['id'] is None or self.parament['id'] == other.parament['id']) \
    #            and self.parament['lastname'] == other.parament['lastname'] \
    #            and self.parament['firstname'] == other.parament['firstname']
    #
    # def id_or_max(self):
    #     if self.parament['id']:
    #         return int(self.parament['id'])
    #     else:
    #         return maxsize