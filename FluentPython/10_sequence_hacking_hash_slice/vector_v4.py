#-*- coding:utf-8 -*-
from array import array
import reprlib
import math
import numbers
import functools
import operator


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        print("type of index: %s" % type(index))
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=self.__class__.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __eq__(self, other):
        # 아래 리턴문 메모리 낭비 새로운 두개의 튜플 객체 생성
        # return tuple(self) == tuple(other)
        if len(self) != len(other):
            return False
        # zip: 반복형 인수의 항목으로 구성된 튜플의 제너레이터를 만든다
        for a, b in zip(self, other):
            if a != b:
                return False
        return True
        
        # using all()
        # return len(self) == len(other) and all(a==b for a, b in zip(self, other))

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        return functools.reduce(lambda a, b: a^b, hashes, 0)


v7 = Vector(range(7))
# print(v7[-1])
# print(v7[1:4])
# print(v7[slice(0,5,2)]):
# print(v7[1, 2])
# print()
