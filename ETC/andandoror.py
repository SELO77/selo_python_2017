def condition(msg, boolean):
    print msg, boolean
    return boolean

print "&& and True True"
if condition("first", True) and condition("second", True):
    print "True"

print "&& and False False"
if condition('first', False) and condition('second', False):
    print "True"

print "&& and True False"
if condition('first', True) and condition('second', False):
    print "True"
