class Foo:
    def hello(self):
        print("Hello")

# without reflection
obj = Foo()
obj.hello()

# reflection
class_name = "Foo"
method = "hello"
obj = globals()[class_name]()
getattr(obj, method)()

# with eval
eval("Foo().hello()")



