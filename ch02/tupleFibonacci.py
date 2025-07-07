def fibonacci():
    # 序列拆解，同時設定多個元素的值
    a, b = 1, 1
    while True:
        yield a  # 暫停執行，需要時再產生一個新元素
        a, b = b, a+b  # 序列拆解，繼續產生一個新元素


# 前十個元素
aObj = fibonacci()
for i in range(10):
    print(aObj.__next__(), end=' ')

# 第一個大於100的元素
for i in fibonacci():
    if i > 100:
        print(i, end=' ')
        break

print(end='\n')

bObj = fibonacci()
print('next(bObj)', next(bObj))
print('next(bObj)', next(bObj))
print('next(bObj)', next(bObj))
print('next(bObj)', next(bObj))