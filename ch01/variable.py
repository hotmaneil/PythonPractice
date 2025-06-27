x = 3
print(type(x))

y = "Hello"
print(type(y))

z = [1, 2, 3]
print(type(z))

# 內建函數-用來測試物件是否為指定類型的實例
resultInt = isinstance(3, int)
print(resultInt)

resultStr = isinstance('Hello', str)
print(resultStr)

a = 3
print(a**2)

a += 6
print(a)

b = [1, 2, 3]
print('b的值為', b)

# 修改列表元素值
b[1] = 5
print(b)
print(b[2])

# 實數相減結果稍微有點偏差
cal = 0.4-0.1
print('實數相減結果稍微有點偏差', cal)

# 預設支援複數運算
c = 3+4j
d = 5+6j
print('預設支援複數運算c+d', c+d)
print('預設支援複數運算c-d', c-d)
print('預設支援複數運算c*d=>這個有疑問', c*d)

print('c/d', c/d)
print('複數的絕對值abs(c)=>這個有疑問', abs(c))

e = -123.56
print('複數的絕對值abs(e)', abs(e))

print('虛部c.imag', c.imag)
print('實部c.real', c.real)
print('c 共軛複數>這個有疑問', c.conjugate())

f = (1, 2, 3)
print('f', f)

# 元組是不可變序列，不支援元素值的修改
# f[1]=5

# Python 允許多個變數指向同一個值：
# 現在h,g是同一個物件，所以記憶體的位址相同
g = 3
print('id(g)', id(g))
h = g
print('id(h)', id(h))

g+=6
print('id(g)', id(g))
print('h', h)
print('id(h)', id(h))
