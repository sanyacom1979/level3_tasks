"""
Сортировка выбором
"""
import math
import random

def one_cycle_sort_vibor(data, idx_begin):
	min = math.inf
	for i in range(idx_begin, len(data)):
		if data[i] < min:
			min = data[i]
			idx_min = i
	data[idx_begin], data[idx_min] = data[idx_min], data[idx_begin]
	

def full_cycle_sort_vibor(data):
	for i in range(len(data) - 1):
		one_cycle_sort_vibor(data, i)
	

if __name__ == "__main__":
	data = [random.randint(1, 20) for _ in range(10)]
	print(f"До сортировки {data}")
	print("_____________________________________")
	full_cycle_sort_vibor(data)
	print(f"После сортировки {data}")