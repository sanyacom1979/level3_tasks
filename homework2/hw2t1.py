import random

class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
        
def add_child_node(head, data):
    tmp = head
    while True:
        if data < tmp.data:
            if not tmp.left:
                tmp.left = Node(data=data)
                break
            else:
                tmp = tmp.left
        elif data > tmp.data:
            if not tmp.right:
                tmp.right = Node(data=data)
                break
            else:
                tmp=tmp.right
        else:
            print(f"Элемент со значением {data} уже есть в дереве")
            break
 


def compare_trees(node1, node2):
    if node1.data != node2.data:
        return "No"
    if node1.left and node2.left:
        res = compare_trees(node1.left, node2.left)
    elif node1.left or node2.left:
        return "No"
    else:
        res = "Yes"
    if res == "Yes":
        if node1.right and node2.right:
            res = compare_trees(node1.right, node2.right)
        elif node1.right or node2.right:
            return "No"
        else:
            return "Yes"
    return res



if __name__ == "__main__":    
    data1 = [[1, 5, 7, 9, 13, 19, 20], [4, 3, 7, 10], [11, 15, 1, 0, 22, 18], [10, 12, 8, 15, 7, 9, 1, 2, 3], [4, 2, 7, 10]]

    data2 = [[5, 9, 19, 13, 20, 7, 1], [4, 3, 7, 10, 11], [1, 2, 3, 7, 11, 15], [10, 12, 8, 15, 7, 9, 1, 2, 3], [4, 3, 7, 11]]
 
    print(data1)
    print(data2)
 
    for t1, t2 in zip(data1, data2):
    
        head1 = Node(data=t1[0])
        head2 = Node(data=t2[0])
        
        build_left = True

        for i in t1[1:]:
            add_child_node(head1, i)
           
        build_left = True

        for i in t2[1:]:
            add_child_node(head2, i)
        
   
        print(compare_trees(head1, head2))

   