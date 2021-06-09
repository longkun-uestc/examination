class A(object):
    _instance = None
    def __init__(self):
        print('这是init函数', self)

    def __new__(cls, *args, **kwargs):
        print('这是cls的id:%d' % id(cls))
        if not cls._instance:
            cls._instance = object.__new__(cls)
        print('这是new函数', cls._instance)
        return cls._instance

a = A()
b = A()
print(a is b)