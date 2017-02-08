import os


print()
print(os.getcwd())
print(__file__.split('/')[-1])


with open('oops.txt', '+r') as f:
    text = f.read()
    print()
    print(text)
    print()

    text.replace('self.TEST_API_URL', 'self.API_URL')

    print()
    print(text)
    print()


print('Done')


import fileinput


filename = 'test_views.py'
replace_set = [('self.TEST_API_URL', 'self.API_URL'), ('self.TEST_VIEW_CLS','self.VIEW_CLS'), ('self.TEST_THROTTLE_CLS', 'self.THROTTLE_CLS')]
count = 0
f = fileinput.FileInput(
    filename,
    inplace=True,
    backup='.bak'
)
for line in f:
    check_list = [i for i, e in enumerate(replace_set) if e[0] in line]

    if check_list:
        for i in check_list:
            line = line.replace(replace_set[i][0], replace_set[i][1])
        count += 1
    print(line, end='')

f.close()