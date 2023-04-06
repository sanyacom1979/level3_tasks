'''
from pprint import pprint 
n = int(input())
m = int(input()) 
field = [] 
for i in range(m):    
	field.append([0] * n) 
# заполняем верх и низ единицами 
for i in range(n): 
    field[i][0] = 1 
for i in range(m): 
    field[0][i] = 1 
for i in range(1, n):    
	for j in range(1, m): 
		field[i][j] = field[i - 1][j] + field[i][j - 1] + field[i - 1][j - 1]
pprint(field)