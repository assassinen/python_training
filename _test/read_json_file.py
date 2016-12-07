__author__ = 'NovikovII'

import json
import os.path

out = 'data/contacts.json'
out = 'data/groups.json'


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', out)
#print(file)

with open(file) as fin:
    res = json.load(fin)

print(len(res))

for i in res:
    #print(i['paramentr']['firstname'])
    print([i for i in i.keys()])
    print([i for i in i.values()])