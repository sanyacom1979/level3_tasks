"""
Поразрядная сортировка
Немного изменил внутренний цикл по сравненнию с l3dz4.py
сделал по компактнее. Правда работает помедленнее.
"""

import random
import time

def max_razryad(data):
    max_k = 0
    for i in data:
        max_k = len(i) if len(i) > max_k else max_k
    return max_k

 

def one_cycle_sort_porrazryad(data, r_num):
    l = [[] for _ in range(10)]
    for i in data:
        if - r_num <= len(i): 
            for j, item in enumerate(l):
                if i[r_num] == str(j):
                    item.append(i)
        else:
            l[0].append(i)
    data = []
    for i in l:
        data += i   
    return data

   
    
def full_cycle_sort_porrazryad(data):
    data = [str(i) for i in data]
    k = max_razryad(data)
    for i in range(-1, -k - 1, -1):
        data = one_cycle_sort_porrazryad(data, i)
    return [int(i) for i in data]


if __name__ == "__main__":
    data = [random.randint(0, 20) for _ in range(10)]
    print(f"До {data}")
    print("__________________________________________")
    data = full_cycle_sort_porrazryad(data)
    print(f"После {data}")