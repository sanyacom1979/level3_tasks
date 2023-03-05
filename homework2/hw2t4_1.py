from operator import add, sub, mul, truediv

class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        
class Stack():
    def __init__(self):
        self.data = []
        
    def push(self, elem):
        self.data.append(elem)
        
    def pop(self):
        if self.data:
            return self.data.pop()


        
def is_operator(data):
    operators = ["+", "-", "*", "/"]
    return data in operators

def is_oper_node(node):
    return is_operator(node.data)


def construct_tree(data):    
    s = Stack()   
    for i in data:
        if is_operator(i):
            x = s.pop()
            y = s.pop()
            s.push(Node(data=i, left=y, right=x))                                  
        else:
            s.push(Node(data=i))
    return s.data[-1]
    


def calc(x, y, o):
    if o == "+":
        return add(x, y)     
    elif o == "-":
        return sub(x, y)        
    elif o == "*":
        return mul(x, y)              
    else:
        return truediv(x, y)



def calc_tree(node):
    if not is_operator(node.data):
        return node.data
    data_left = calc_tree(node.left)
    data_right = calc_tree(node.right)
    return calc(data_left, data_right, node.data)


if __name__ == "__main__":
    #data = [10, 5, "-", 5, "*", 21, 7, "/", "+"]
    #data = [1, 3, "+", 2, 8, 1, "*", "+", "*", 10, 2, "-", "+"]
    #data = [11, 5, "-", 6, 2, "*", 7, "+", "*", 15, 5, "-", "+"]
    #data = [20, 2, "-", 5, 2, "-", 3, 9, 15, "+", "*", "+", "*", 15, 21, 7, "/", "-", "+"]
    data = [10, 4, "-", 3, 7, "+", 2, 9, 3, "-", "*", "*", 5, "-", "*", 15, 10, 2, "+", 5, "-", "-", "*"]
    print(data)
    head = construct_tree(data)
  
    print(calc_tree(head))