from multiprocessing import Process, Event


def f(thidEvent, i):
    if thidEvent.is_set():
        thidEvent.wait()
        print('hello world', i)
        thidEvent.clear()
    else:
        thidEvent.set()


if __name__ == '__main__':
    e = Event()
    for num in range(10):
        Process(target=f, args=(e, num)).start()
