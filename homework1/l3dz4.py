"""
Поразрядная сортировка
"""

import random
import time


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
    data = [random.randint(0, 20) for _ in range(10)]
    print(f"До {data}")
    print("__________________________________________")
    data = full_cycle_sort_porrazryad(data)
    print(f"После {data}")