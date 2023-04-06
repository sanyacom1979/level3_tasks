import time

def fibo(n):
	
	if n == 0 or n == 1:
		return n
	return fibo(n - 1) + fibo(n - 2)



if __name__ == "__main__":
	print(fibo(3))
	print(fibo(7))
	print(fibo(9))
	start = time.time()
	print(fibo(40))
	print(time.time() - start)