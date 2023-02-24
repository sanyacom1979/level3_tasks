"""
Связный список с методами печати
и добавления в конец списка
"""

import random

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
 
def print_all_nodes(head):
    print(f"[{head.data}] -> ", end="")
    tmp = head
    while tmp.next:
        tmp = tmp.next
        print(f"{tmp.data} -> ", end="")
        

def add_node(tail, new_elem):
    tail.next = new_elem
    return new_elem
    
 
head = Node(data=1)
tail = head

for i in range(10):
    new_node = Node(data=random.randint(0, 10))
    tail = add_node(tail, new_node)
print_all_nodes(head)
print("")

