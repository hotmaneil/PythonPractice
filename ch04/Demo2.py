import types


class Demo2:
    pass


t = Demo2()


def test(self, Value):
    self.value = Value


# 動態增加普通函數
t.test = test
print(t.test)

t.test(t, 3)
print(t.value)


# 動態增加繫結的方法
t.test = types.MethodType(test, t)
print(t.test)

t.test(5)
print(t.value)
