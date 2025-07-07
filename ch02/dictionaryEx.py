a_dict = {'server': 'xxx', 'database': 'mysql'}
print('a_dict', a_dict)

# 使用內建函數dict()透過既有資料快速建立字典
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
dictionary = dict(zip(keys, values))
print('dictionary', dictionary)

# 空字典
x = dict()
print('x', x)

# 查看物件類型
print('type(x)', type(x))

# 空字典
y = {}

# 根據給定的「鍵：值」建立字典
myDic = dict(name='Neil', age=38)
print('myDic-1', myDic)

# 修改元素值
myDic['age'] = 38.5
print('myDic-2', myDic)

# 增加新元素
myDic['address'] = 'TauYuan'
print('myDic-3', myDic)

# 返回所有元素
print('返回所有元素', myDic.items())

# update()
myDic.update({'Phone': 'note9', 'age': 38.9})
print('myDic-4', myDic)

# 刪除字典元素
del myDic['age']
print('myDic-5', myDic)

# 刪除整個字典
# del myDic
# print('myDic-6', myDic)
print('彈出', myDic.popitem())
print('myDic-6', myDic)

# 彈出指定鍵對應的元素
myDic.pop('address')
print('myDic-7', myDic)

print('存取字典物件的資料', myDic['name'])

# 判斷字典中是否存在指定的「鍵」
if 'age' in myDic:
    print(myDic['Age'])
else:
    print('No Exists.')

# 或是處理異常結構
try:
    print(myDic['Age'])
except:
    print('No Exists.')

# 若字典存在該「鍵」，則返回對應的「值」
print('若字典存在該「鍵」，則返回對應的「值」', myDic.get('name'))

# 指定的「鍵」不存在時，返回指定的預設值
getIf = myDic.get('Age', 'No Exists.')
print('getIf', getIf)

# setdefault()方法返回指定「鍵」對應的「值」，若不存在增加一個新元素
myDic.setdefault('weight', 65)
print('myDic-8', myDic)

# 預設巡訪字典的「鍵」
for item in myDic:
    print('key', item)

# 明確指定巡訪字典的元素
for item in myDic.items():
    print(item)

print('myDic.items()',myDic.items()) 

print('myDic.keys()',myDic.keys()) 

print('myDic.values()',myDic.values()) 


# 以給定內容為「鍵」，建立「鍵」為空的字典
onlyKeyDict = dict.fromkeys(['name', 'age', 'sex'])
print('onlyKeyDict', onlyKeyDict)
