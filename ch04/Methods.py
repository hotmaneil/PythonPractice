class Root:
    __total = 0

    # 建構函式
    def __init__(self, Value):
        self.__value = Value
        Root.__total += 1

    # 普通的實例方法
    def show(self):
        print('self.__value:', self.__value)
        print('Root.__total:', Root.__total)

    # 修飾器，宣告類別方法
    @classmethod
    def classShowTotal(cls):
        print('cls total',cls.__total)

    # 修飾器，宣告靜態方法
    @staticmethod
    def staticShowTotal():
        print('Root total',Root.__total)


print('第1個')
root = Root(3)
root.classShowTotal()
root.staticShowTotal()

root.show()

print('第2個')
rr = Root(5)

Root.classShowTotal()
Root.staticShowTotal()

# Root.show()=>錯，以下是正確
Root.show(root)
root.show()

Root.show(rr)
rr.show()
