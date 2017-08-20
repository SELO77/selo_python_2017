class Foo:
    def hello(self):
        print("Hello")

# without reflection
obj = Foo()
obj.hello()

# reflection
class_name = "Foo"
method = "hello"
current_namespace = globals()
print(type(current_namespace))
if isinstance(current_namespace, dict):
    copy_namespace = current_namespace.copy()
    print('====')
    for k, v in copy_namespace.items():
        print(k, v)
    print('====')
else:
    print(current_namespace)
obj = globals()[class_name]()
getattr(obj, method)()

# with eval
eval("Foo().hello()")



