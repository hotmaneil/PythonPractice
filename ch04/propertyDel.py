# 可以將屬性設為可讀、可修改與可刪除
class Test:
    def __init__(self, value):
        self.__value = value

    # 讀取私有資料成員的值
    def __get(self):
        return self.__value

    # 修改私有資料成員的值
    def __set(self, v):
        self.__value = v

    # 刪除物件的私有資料成員
    def __del(self):
        del self.__value

    # 可讀可寫屬性，指定對應的讀寫方法
    value = property(__get, __set, __del)

    def show(self):
        print(self.__value)


t = Test(3)
t.show()
print(t.value)

t.value = 5
t.show()
print(t.value)

del t.value
#已刪除
