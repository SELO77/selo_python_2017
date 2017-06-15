class cached_property(object):
    """
    Decorator that converts a method with a single self argument into a
    property cached on the instance.
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, type=None):
        if instance is None:
            return self
        # monkey patch
        res = instance.__dict__[self.func.__name__] = self.func(instance)
        return res



class Test(object):

    @cached_property
    def p(self):
        return "Hello"


if __name__ == "__main__":
    t = Test()
    p = t.p
    print(p)
    s = t.p