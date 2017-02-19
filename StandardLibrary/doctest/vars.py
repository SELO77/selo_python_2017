def do(text='default'):
    count = 0
    print(text, count)
    print()
    print('vars', vars())
    print('locals', locals())
    return text, count

do('yabayb')
