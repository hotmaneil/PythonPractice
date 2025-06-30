import random
import time

#產生成列表
x = list(range(10000))	

#產生成集合
y = set(range(10000))	

#產生成字典
z = dict(zip(range(10000),range(10000)))		

#產生成亂數
r = random.randint(0, 9999)	

#測試清單列表中是否包含某個元素
start = time.time()
for i in range(9999):
    r in x 				
print('list,time used:', time.time()-start)

#測試集合中是否包含某個元素
start = time.time()
for i in range(9999):
    r in y					
print('set,time used:', time.time()-start)

#測試字典中是否包含某個元素
start = time.time()
for i in range(9999):
    r in z					
print('dict,time used:', time.time()-start)
