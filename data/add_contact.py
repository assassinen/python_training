__author__ = 'NovikovII'

from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits #+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# testdata = [Contact(firstname=firstname, \
#                     middlename=random_string("", 10), \
#                     work=random_string("", 10), \
#                     mobile=random_string("", 10), \
#                     address=random_string("", 10), \
#                     lastname=random_string("", 10))
#             for firstname in ["", random_string("", 10)]
#             for address in ["", random_string("", 10)]
# ]

n = 1

testdata = [Contact(firstname=firstname, \
                    middlename=random_string("", 10), \
                    work=random_string("", 10), \
                    mobile=random_string("", 10), \
                    address=random_string("", 10), \
                    lastname=random_string("", 10))
            for firstname in ["", random_string("", 10)]
            for address in ["", random_string("", 10)]
            for i in range(n)
]

err_date = [Contact(firstname=" Mdz k", lastname="zCQ ")]

constant = [Contact(firstname="Алексей", \
                    middlename="Иларионовна", \
                    lastname="Баранцев", \
                    work="суперпрепод", \
                    address="Не дом и не улица", \
                    mobile='8915223344')]

