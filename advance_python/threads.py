from time import sleep, perf_counter

import threading


def task(a):
    print('Starting a task...',a)
    sleep(10)
    print(threading.current_thread().name)
    while True:
        c = 1+1

    print('done')


start_time = perf_counter()

from threading import Thread

t2 = Thread(target=task)

i = 0
while True:
    thread = Thread(target=task, args=[str(i)])
    thread.name = str(i)
    i = i+1
    thread.start()
    sleep(0)