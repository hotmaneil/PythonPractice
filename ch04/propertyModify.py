# 把屬性設為可讀、可修改，但不允許刪除
class Test:
    def __init__(self, value):
        self.__value = value

    # 讀取私有資料成員的值
    def __get(self):
        return self.__value

    # 修改私有資料成員的值
    def __set(self, v):
        self.__value = v

    # 可讀可寫屬性，指定對應的讀寫方法
    value = property(__get, __set)

    def show(self):
        print(self.__value)


t = Test(3)

# 允許讀取屬性值
print(t.value)

# 允許修改屬性值
t.value = 5
print(t.value)

t.show()

# 試圖刪除屬性失敗
# del t.value
