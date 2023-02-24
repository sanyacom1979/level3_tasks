"""
Разворот связного списка
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
 
 
def reverse_all_nodes(head):
    cur_data_lst = []
    tmp = head
    while tmp.next:
        cur_data_lst.append(tmp)
        tmp = tmp.next
    for i in range(len(cur_data_lst) - 1, -1, -1):
        tmp.next = cur_data_lst[i]
        tmp = tmp.next
    tmp.next = None


head = Node(data=1)
tail = head

for i in range(10):
    new_node = Node(data=random.randint(0, 10))
    tail = add_node(tail, new_node)
print("До разворота...")
print_all_nodes(head)
print("")
reverse_all_nodes(head)
print("После разворота...")
print_all_nodes(tail)
print("")

