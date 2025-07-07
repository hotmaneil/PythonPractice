# 元組
x = (1, 2, 3)
print('x', x)

# 使用type()函數查看變數類型
print('type(x)', type(x))

# 如果元組只有一個元素，必須在後面多寫一個逗號
y = (3,)
print('y', y)

# 空元組
z = ()

# 空元組
a = tuple()

# 將其它反覆運算物件轉換為元組
myTuple = tuple(range(5))
print('myTuple', myTuple)

# 建立生成器物件
generateObj = ((i+2)**2 for i in range(10))
print('generateObj', generateObj)

result=tuple(generateObj)
print('result',result)

# 生成器物件已巡訪結束，沒有元素了
print('list(generateObj)',list(generateObj))

# 使用生成器物件的__next__()方法取得元素
generateObj = ((i+2)**2 for i in range(10))
print('generateObj.__next__()-1',generateObj.__next__())
print('generateObj.__next__()-2',generateObj.__next__())

#以迴圈直接巡訪生成器物件的元素
generateObj = ((i+2)**2 for i in range(10))
for item in generateObj:
    print(item,end=' ')