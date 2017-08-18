class Human(object):

    def __init__(self):
        print("__init__")

    def __del__(self):
        print("__del__")

class Earth(object):

    def __init__(self):
        print("earth init")
        h = Human()

    def __del__(self):
        print("earth del")

s = "SELO"



if __name__ == '__main__':
    e = Earth()
    print(e.__class__)
    e.__class__._test = 't!!!!!!!!!!!!!!'
    print(e.__class__._test)
    print(e._test)
