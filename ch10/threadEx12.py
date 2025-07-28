from multiprocessing import Process, Manager


def myFunction(data, l, t):
    data['name'] = 'Dong Fuguo'
    data['age'] = 38
    data['sex'] = 'Male'
    data['affiliation'] = 'SDIBT'
    l.reverse()
    t.value = 3


if __name__ == '__main__':
    with Manager() as manager:
        thisDict = manager.dict()
        l = manager.list(range(10))
        t = manager.Value('i', 0)
        p = Process(target=myFunction, args=(thisDict, l, t))
        p.start()
        p.join()
        for item in thisDict.items():
            print(item)
        print(l)
        print(t.value)
