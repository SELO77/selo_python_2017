class First(object):
    def __init__(self):
        print("@1", self.__class__.__name__)

    def dispatch(self):
        print('@1 dispatch')


class Second(object):
    # def __init__(self):
    #     print("@2", self.__class__.__name__)

    def dispatch(self):
        print('@2 dispatch')


class Third(Second, First):
    pass
    # def __init__(self):
    #     print("@", self.__class__.__name__)


third = Third()
third.dispatch()