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
        

def height_tree(node, h_max=-1, h_cur=-1):
    h_max, h_cur = (h_max + 1, h_cur + 1) if h_max == h_cur else (h_max, h_cur + 1)
    if node.left:
        h_max, h_cur = height_tree(node.left, h_max, h_cur)
    print(node.data, end="  ")
    if node.right:
        h_max, h_cur = height_tree(node.right, h_max, h_cur)
    h_cur -= 1
    return h_max, h_cur

if __name__ == "__main__":    
    data = [random.randint(0, 20) for _ in range(10)]
 
    print(data)
 
    head = Node(data=data[0])
 
    for i in data[1:]:
        add_child_node(head, i)
    
    print(sorted(data))
 
    h_max, h_cur = height_tree(head)

    print("")
 
    print(f"Высота дерева (h_max) = {h_max}")