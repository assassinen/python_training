__author__ = 'NovikovII'


from point import Point
import string
import random




# #random_contact()
# print(random_contact())
#
#
# testdata = [
#     (str(n1)+str(n2)+str(n3)+str(n4))
#     for n1 in range (10)
#     for n2 in range (10)
#     for n3 in range (10)
#     for n4 in range (10)
# ]
#
# for i in testdata:
#     print(i)

#print(''.join([random.choice(string.ascii_letters + string.digits) for i in range(random.randrange(20))]))

#map
# l1 = [Point(i, i*i) for i in range(-5,6)]
#
# l2 = list(map(lambda i: Point(i, i*i), range(-5,6)))
# l3 = list(map(lambda p: Point(p.x, -p.y), l1))
# print(l1)
# print(l2)
# print(l3)
#
# #filter
# l3 = list(filter(lambda p: p.x > 0, l1))
# print(l3)
#
# l3 = list(filter(lambda p: p.x % 2 == 0, l1))
# print(l3)
#
# l3 = [i for i in range(0,5)]
# print(l3)
#
# print(l3[0:2])
# print(l3[0])
#
# l3[0:2] = []
# print(l3)


# циклы
# l = []
# l2 = []
#
# for i in range(-5, 6):
#     l.append(Point(i, i*i))
#
# for el in l:
#     l2.append(Point(el.x, -el.y))
#
# l3 = [Point(i, i*i) for i in range(-5, 6)]
#
# print(l)
# print(l2)
# print(l3)

#сортировка списков
#l1 = [Point(2,1), Point(1,2), Point(0,0)]
# def y(p):
#     return p.y

# print(l1)
# l2 = sorted(l1, key=lambda p: p.x)
# print(l2)
# l2 = sorted(l1, key=y)
# print(l2)


