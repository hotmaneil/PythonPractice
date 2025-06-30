import random
import time


def RandomNumbers1(number, start, end):
    '''使用列表來產生成number個介於start和end之間的不重複亂數'''
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            break
    return data


def RandomNumbers2(number, start, end):
    '''使用集合來產生成number個介於start和end之間的不重複亂數'''
    data = set()
    while True:
        element = random.randint(start, end)
        data.add(element)
        if len(data) == number:
            return data


def RandomTest():
    '''測試random.sample'''
    elements = random.sample(range(1000), 20)
    return elements
    # data = set()
    # while True:
    #     element = random.sample(range(1000), 20)
    #     data.add(element)
    #     return data


start = time.time()
for i in range(1000):
    d1 = RandomNumbers1(500, 1, 1000)
print('Time used:', time.time()-start)

start = time.time()
for i in range(1000):
    d2 = RandomNumbers2(500, 1, 1000)
print('Time used:', time.time()-start)

collection3 = RandomTest()
print('collection3', collection3)
