"""
Быстрая сортировка
"""
import math
import random

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
	data = [random.randint(1, 20) for _ in range(10)]
	print(f"До {data}")
	print("_________________________________")
	fast_sort(data)
	print(f"После {data}")