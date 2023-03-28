import threading
import time

class CustomThread(threading.Thread):

	def __init__(self, limit):
		threading.Thread.__init__(self) 
		self._limit = limit

	def run(self):
		for i in range(self._limit):
			print(f"from CustomThread: {i}")
			time.sleep(0.5)




cth = CustomThread(3)
cth.start()

