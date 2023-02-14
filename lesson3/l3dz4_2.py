"""
Сравнение времени выполнения сортировки
выбором, быстрой сортировки и поразрядной сортировки
при разных сравниваемых диапазонах
""" 

import math
import random
import time


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


def max_razryad(data):
    max_k = 0
    for i in data:
        max_k = len(i) if len(i) > max_k else max_k
    return max_k



def one_cycle_sort_porrazryad(data, r_num):
    l0 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    l7 = []
    l8 = []
    l9 = []
    for i in data:
        if - r_num <= len(i): 
            if i[r_num] == "0":
                l0.append(i)
            if i[r_num] == "1":
                l1.append(i)
            if i[r_num] == "2":
                l2.append(i)
            if i[r_num] == "3":
                l3.append(i)
            if i[r_num] == "4":
                l4.append(i)
            if i[r_num] == "5":
                l5.append(i)
            if i[r_num] == "6":
                l6.append(i)
            if i[r_num] == "7":
                l7.append(i)
            if i[r_num] == "8":
                l8.append(i)
            if i[r_num] == "9":
                l9.append(i)
        else:
            l0.append(i)
    return l0 + l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9
 

    
def full_cycle_sort_porrazryad(data):
    data = [str(i) for i in data]
    k = max_razryad(data)
    for i in range(-1, -k - 1, -1):
        data = one_cycle_sort_porrazryad(data, i)
    return [int(i) for i in data]



if __name__ == "__main__":
	len_data = [10, 1000, 10000, 100000]
	
	print("Cортировка выбором")
	for i in len_data:
		print("Двузначные числа")
		data = [random.randint(10, 10**2) for _ in range(i)]
		time_start = time.time()
		full_cycle_sort_vibor(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Трехзначные числа")
		data = [random.randint(10**2, 10**3) for _ in range(i)]
		time_start = time.time()
		full_cycle_sort_vibor(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Десятизначные числа")
		data = [random.randint(10**9, 10**10) for _ in range(i)]
		time_start = time.time()
		full_cycle_sort_vibor(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Тысячазначные числа")
		data = [random.randint(10**999, 10**1000) for _ in range(i)]
		time_start = time.time()
		full_cycle_sort_vibor(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
	print("________________________________________________________________________")
	print("Быстрая сортировка")
	for i in len_data:
		print("Двузначные числа")
		data = [random.randint(10, 10**2) for _ in range(i)]
		time_start = time.time()
		fast_sort(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Трехзначные числа")
		data = [random.randint(10**2, 10**3) for _ in range(i)]
		time_start = time.time()
		fast_sort(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Десятизначные числа")
		data = [random.randint(10**9, 10**10) for _ in range(i)]
		time_start = time.time()
		fast_sort(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Тысячазначные числа")
		data = [random.randint(10**999, 10**1000) for _ in range(i)]
		time_start = time.time()
		fast_sort(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
	print("________________________________________________________________________")
	print("Поразрядная сортировка")
	for i in len_data:
		print("Двузначные числа")
		data = [random.randint(10, 10**2) for _ in range(i)]
		time_start = time.time()
		data = full_cycle_sort_porrazryad(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Трехзначные числа")
		data = [random.randint(10**2, 10**3) for _ in range(i)]
		time_start = time.time()
		data = full_cycle_sort_porrazryad(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Десятизначные числа")
		data = [random.randint(10**9, 10**10) for _ in range(i)]
		time_start = time.time()
		data = full_cycle_sort_porrazryad(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")
		print("Тысячазначные числа")
		data = [random.randint(10**999, 10**1000) for _ in range(i)]
		time_start = time.time()
		data = full_cycle_sort_porrazryad(data)
		print(f"Размер списка = {i}, время выполнения = {time.time() - time_start}")
		print("===================================================================")