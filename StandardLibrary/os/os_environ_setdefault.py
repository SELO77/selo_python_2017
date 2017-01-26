

import os
test_flag_key = 'MMT_UNIT_TESTING'
if  os.environ.get(test_flag_key, None):
    print(os.environ['MMT_UNIT_TESTING'])
else:
    os.environ.setdefault(test_flag_key, 'Yes')

print('1', os.environ['MMT_UNIT_TESTING'])
print('2', os.environ.pop('MMT_UNIT_TESTING'))
print('3', os.environ['MMT_UNIT_TESTING'])


