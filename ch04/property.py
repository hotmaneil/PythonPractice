class Test:
    def __init__(self, value):
        self.__value = value

    # 修飾器，定義屬性，提供對私有資料成員的存取
    @property
    def value(self):
        return self.__value


t = Test(3)
print(t.value)

# 唯讀屬性不允許修改
# t.value=5

# 動態增加新成員
t.v = 5
print(t.v)

# 動態刪除成員
del t.v

# 試圖刪除物件屬性失敗
# del t.value
