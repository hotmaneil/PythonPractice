# 定義一個類別，繼承自object類別
class Car(object):

    # 定義成員方法
    def infor(self):
        print('This is a car')


# 產生實體物件
mycar = Car()

# 呼叫物件的方法
mycar.infor()

# 測試一個物件是否為某類別的實例
result1 = isinstance(mycar, Car)
print('result1', result1)
