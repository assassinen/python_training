__author__ = 'NovikovII'

from model.contact import Contact
import random
import string
import jsonpickle
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    getopt.usage()
    sys.exit(2)

n = 1
out = 'data/contacts.json'

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        out = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=firstname, \
                    middlename=random_string("", 10), \
                    work=random_string("", 10), \
                    mobile=random_string("", 10), \
                    address=random_string("", 10), \
                    lastname=random_string("", 10))
            for firstname in ["", random_string("", 10)]
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', out)

with open(file, 'w') as out:
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))