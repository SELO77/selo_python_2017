class StrKeyDict0(dict):


    def __missing__(self, key):
        print("__missing__()", key)
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]


    def get(self, key, d=None):
        print("get()", key)
        try:
            return self[key]
        except KeyError:
            print('get() KeyError')
            return d


    def __contains__(self, key):
        print('__contains__()', key)
        return key in self.keys() or str(key) in self.keys()

selo = StrKeyDict0(name="selo", sex='m')
selo.update({'123': 456})
print(selo)
print()
# print(selo["hello"])
'none_key' in selo
print(selo.keys())
print(type(selo.keys()))