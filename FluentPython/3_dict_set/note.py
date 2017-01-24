my_dict = {}
import collections
from collections import abc
isinstance(my_dict, collections.abc.Mapping)

tt = (1, 2, (30, 40))
print(hash(tt))
# tl = (1, 2, [30, 40])
# print(hash(tl))
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

index = collections.defaultdict(list)

str()


counter1 = collections.Counter('abaaaaaaaaabbbbbbbcccccc')
print(counter1)
order_d = collections.OrderedDict({'name': 'selo', 'age': 'm'})
print(order_d)

collections.UserDict()