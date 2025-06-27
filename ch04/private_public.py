class Ex:
    #建構函數
    def __init__(self,value1=0,value2=0):
        self._value1=value1

        #私有成員
        self.__value2=value2

    #成員方法
    def setValue(self,value1,value2):
        self._value1=value1

        #類別內部可以直接存取私有成員
        self.__value2=value2

    def show(self):
        print(self._value1)
        print(self.__value2)


ex1=Ex()

#類別外部可以直接存取非私有成員
print(ex1._value1)



    