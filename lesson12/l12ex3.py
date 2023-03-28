
from threading import Thread, Lock
import time

DATA = [1]

LOCK = Lock()

def increase():
	while LOCK.locked():
		print("Ждем...")
		time.sleep(1)
	LOCK.acquire()
	print("Работаем...")
	for _ in range(5):		
		elem = DATA.pop()
		time.sleep(1)
		elem += 10
		DATA.append(elem)
	LOCK.release()
		

x1 = Thread(target=increase)
x2 = Thread(target=increase)
x3 = Thread(target=increase)
x4 = Thread(target=increase)
x5 = Thread(target=increase)

x1.start()
x2.start()
x3.start()
x4.start()
x5.start()

time.sleep(60)
print(DATA)