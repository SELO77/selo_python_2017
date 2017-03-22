def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()


print('\x1b[4;37;46m' + 'Success!' + '\x1b[0m')
print('\x1b[3;30;43m' + 'Success!' + '\x1b[0m')
print('\x1b[1;37;41m' + 'Success!' + '\x1b[0m')

