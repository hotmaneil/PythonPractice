class Car(object):

    # 屬於類別的資料成員
    price = 10000

    def __init__(self, Color):
        # 屬於物件的資料成員
        self.color = Color


# 產生實體物件
myCar1 = Car("Red")
myCar2 = Car("Blue")
print(myCar1.color, myCar1.price)

# 修改類別屬性
Car.price = 11000
Car.name = 'Luxgen'

# 修改實例屬性
myCar1.color = 'Yellow'
print(myCar2.color, Car.price, Car.name)
print(myCar1.color, Car.price, Car.name)
