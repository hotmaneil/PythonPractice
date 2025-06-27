class Demo(object):
    total = 0

    # 該方法在__init__()之前被呼叫
    def __new__(cls, *args, **kwargs):
        if cls.total >= 3:
            raise Exception('最多只能建立3個物件')
        else:
            return object.__new__(cls)

    def __init__(self):
        Demo.total = Demo.total+1


t1 = Demo()
print(t1)

t2 = Demo()
t3 = Demo()
t4 = Demo()
