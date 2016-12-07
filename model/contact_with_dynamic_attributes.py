__author__ = 'NovikovII'

from sys import maxsize

class Contact:
    def __init__(self, **kwargs):
        self.paramentr = {'id': None, 'lastname': None, 'firstname': None}
        for key, item in kwargs.items():
            self.paramentr[key] = item

    def __repr__(self):
        return "%s: %s %s" % (self.paramentr['id'], self.paramentr['lastname'],  self.paramentr['firstname'])

    def __eq__(self, other):
        return (self.paramentr['id'] is None or other.parament['id'] is None or self.paramentr['id'] == other.parament['id']) \
               and self.paramentr['lastname'] == other.parament['lastname'] \
               and self.paramentr['firstname'] == other.parament['firstname']

    def id_or_max(self):
        if self.paramentr['id']:
            return int(self.paramentr['id'])
        else:
            return maxsize