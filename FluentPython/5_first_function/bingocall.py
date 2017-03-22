import random


class BingoCage:


    # def __new__(cls, *args, **kwargs):
    #     print('__new__')


    def __init__(self, items):
        print('__init__')
        self._items = list(items)
        random.shuffle(self._items)


    def pick(self):
        print('pick')
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')


    def __call__(self):
        print('__call__')
        return self.pick()
