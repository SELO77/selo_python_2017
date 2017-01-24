class selodict(dict):
    default_value = []
    def __missing__(self, *args):
        print('call __missing__')
        print(args)
        self.update({'hello': self.default_value})
        return self['hello']


sd = selodict({'name': 'selo', 'sex': 'M'})
print(sd)
sd2 = selodict(name='serim', sex='F')
print(sd2)

sd['hello'].append((1,2,3))
print(sd)
