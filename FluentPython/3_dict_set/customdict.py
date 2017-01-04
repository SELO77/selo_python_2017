class selodict(dict):

    def __missing__(self, *args):
        print('call __missing__')
        print(args)
        self.update({'hello': 'default_value'})
        return self['hello']


sd = selodict({'name': 'selo', 'sex': 'M'})
print(sd)
sd2 = selodict(name='serim', sex='F')
print(sd2)


print(sd['hello'])
