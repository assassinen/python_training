__author__ = 'NovikovII'

from sys import maxsize

class Contact:
    def __init__(self, lastname=None, middlename=None, firstname=None, id=None, address=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None):
        self.lastname = lastname 
        self.firstname = firstname
        self.middlename = middlename
        self.id = id
        self.address = address
        self.home = home 
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        
    def __repr__(self):
        return "%s: %s %s" % (self.id, self.lastname,  self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
        