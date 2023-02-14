'''
import math
lst = [100, 40, 60, 20, 70]
min = math.inf
for i in range(len(lst)):
	if lst[i] < min:
		min = lst[i]
print(min)
'''