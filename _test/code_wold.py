__author__ = 'NovikovII'

import string
import time
import hashlib



symbols = [i for i in string.ascii_letters[0:25]]

#c_time = int(time.strftime("%Y%m%d%H%M%S", time.localtime()))*1000 + round(time.time() * 1000) % 1000
c_time = int(time.strftime("%H%M%S", time.localtime()))

print(c_time)


a = ("".join((i1,i2,i3,i4,i5,i6,i7,i8,i9,i0))
            for i1 in symbols
            for i2 in symbols
            for i3 in symbols
            for i4 in symbols
            for i5 in symbols
            for i6 in symbols
            for i7 in symbols
            for i8 in symbols
            for i9 in symbols
            for i0 in symbols
)
n = 0

md5 = 'ecbfb9d98a676f3d75f5931035a87207'
print(len(md5))
