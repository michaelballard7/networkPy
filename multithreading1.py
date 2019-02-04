
from threading import Thread
import time


def f1():
    print("Hi from f1\n")
    time.sleep(5)
    print("Hi Im F1 and im finally awoke")


t1 = Thread(target=f1)
t1.start()

print("Hi from main")
time.sleep(5)
print("The main proccess is awoke")
t1.join()


for i in range(10):
    t = Thread(target=f1)
    t.start()
