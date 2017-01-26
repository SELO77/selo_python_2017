from importlib import import_module

import_str = 'importtest'

module = import_module(import_str)
print(type(module))
print(dir(module))
for k in dir(module):
    print(k)
    locals()[k] = getattr(module, k)
print(module.IMPORT_LITERAL)

# print(locals())
print(globals())
# print(type(locals()))
# print(locals()[''])
print()

module2 = __import__(import_str, globals(), locals(), ['*'])
print(type(module2))
print(module is module2)
print(module2.IMPORT_LITERAL)