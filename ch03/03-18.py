#第一種
def demo(lst, k):
    x = lst[:k]
    x.reverse()
    y = lst[k:]
    y.reverse()
    r = x+y
    return list(reversed(r))

#第二種
def demoReform(lst, k):
    temp = lst[:]
    for i in range(k):
        temp.append(temp.pop(0))
    return temp

lst = list(range(1, 21))
# print(lst)
# print(demo(lst, 5))

print(demoReform(lst, 5))
