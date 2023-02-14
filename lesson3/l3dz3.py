"""
Сравнение времени выполнения сортировки
выбором и быстрой сортировки
""" 

import math
import random
import time
from matplotlib import pyplot as plt

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


def fast_sort(data, left=0, right=math.inf):
	right = len(data) - 1 if right == math.inf else right
	if left != right:
		target_idx = math.ceil((left + right)/2)
		i = left
		while i <= right:
			if i <= target_idx:
				if data[i] > data[target_idx]:
					data.insert(right, data.pop(i))
					target_idx -= 1
				else:
					i += 1
			elif i > target_idx:
				if data[i] < data[target_idx]:
					data.insert(target_idx, data.pop(i))
					target_idx += 1
				i += 1
		if target_idx != left:
			fast_sort(data, left, target_idx - 1)
		if target_idx != right:
			fast_sort(data, target_idx + 1, right)


if __name__ == "__main__":
	x_data = [10, 1000, 10000, 100000]
	y_data_vibor = []
	y_data_fast = []
	print("Cортировка выбором")
	for i in x_data:
		data = [random.randint(1, i * 2) for _ in range(i)]
		time_start = time.time()
		full_cycle_sort_vibor(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		y_data_vibor.append(time.time() - time_start)
	print("________________________________________________________________________")
	print("Быстрая сортировка")
	for i in x_data:
		data = [random.randint(1, i * 2) for _ in range(i)]
		time_start = time.time()
		fast_sort(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		y_data_fast.append(time.time() - time_start)

	plt.plot(x_data, y_data_vibor, color="r", label="vibor")
	plt.plot(x_data, y_data_fast, color="g", label="fast")
	plt.legend()
	plt.show()
