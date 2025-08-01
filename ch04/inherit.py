# 人
class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        # 透過呼叫方法進行初始化，這樣可以對參數進行更好的控制
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            print('name must be string.')
            # 若資料不合法就使用預設值
            self.__name = ''
            return
        self.__name = name

    def setAge(self, age):
        if type(age) != int:
            print('age must be integer.')
            self.__age = 20
            return
        self.__age = age

    def setSex(self, sex):
        if sex not in ('man', 'woman'):
            print('')
            self.__sex = 'man'
            return
        self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex, sep='\n')

# 教師


class Teacher(Person):
    def __init__(self, name='', age=30, sex='man', department='IT'):
        # super().__init__(name, age, sex)
        # 呼叫基礎類別建構方法，初始化相關的私有資料成員
        super(Teacher, self).__init__(name, age, sex)

        # 也可以這樣初始化基礎類別的私有資料成員
        # Person.__init__(self,name,age,sex)

        # 初始化衍生類別的資料成員
        self.setDepartment(department)

    def setDepartment(self, department):
        if type(department) != str:
            print('department must be a string.')
            self.__department = 'IT'
            return
        self.__department = department

    def show(self):
        super(Teacher, self).show()
        print(self.__department)


if __name__ == '__main__':
    # 建立基礎類別物件：
    employee = Person('Neil', 30, 'man')
    employee.show()

    # 建立衍生類別物件：
    education = Teacher('Lisa', 20, 'woman', 'Manage')
    education.show()
    education.setAge(40)
    education.show()
