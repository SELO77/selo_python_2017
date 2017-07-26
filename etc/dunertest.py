__gvar = 0
_gvar = 0
class C:
    # def method_a(self):
    #     global __gvar
    #     __gvar += 1
    #     return __gvar

    # def method_a(self):
    #     global _gvar
    #     _gvar += 1
    #     return _gvar

    # def method_a(self):
    #     if not hasattr(self, '__attr'):
    #         self.__attr = 0
    #         print('__attr created!!', self.__attr)
    #
    #
    #     self.__attr += 1
    #     return self.__attr
    #
    # def method_a(self):
    #     if not hasattr(self, '_attr'):
    #         self._attr = 0
    #         print('_attr created!!', self._attr)
    #
    #     self._attr += 1
    #     return self._attr

    def __init__(self):
        self.a = 123
        self._a = 123
        self.__a = 123
        print('========')
        print(self.a)
        print(self._a)
        print(self.__a)
        print('========')

# def empty_function():
#     global g_test2
#     g_test2 = 2
#
# empty_function()


if __name__ == '__main__':

    d = C()
    print(d.a)
    print(d._a)
    d._a = 2
    print(d._a)
    print(d._C__a)
    d._C__a = 3
    print(d._C__a)
    # print(d.method_a())
    # print(d.method_a())