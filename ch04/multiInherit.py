class A():
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private method of A')

    def public(self):
        print('public() method of A')

    def __test(self):
        print('__test() method of A')

#注意：B類別沒有建構函數
class B(A):
    def __private(self):
        print('__private method of B')

    def public(self):
        print('public() method of B')

#建立衍生類別物件
b=B()

class C(A):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private method of C')

    def public(self):
        print('public() method of C')

# c=C()
