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
        return add(y, x)     
    elif o == "-":
        return sub(y, x)        
    elif o == "*":
        return mul(y, x)              
    else:
        return truediv(y, x)



def calc_tree(node, s_num, s_oper, s_iter):
    result = 0
    if node.left:
        if is_oper_node(node.left):
            s_iter.push(0)
        result = calc_tree(node.left, s_num, s_oper, s_iter)
        
    if isinstance(node.data, int):
        s_num.push(node.data)
    else:
        s_oper.push(node.data)
    
    if node.right:
        if is_oper_node(node.right):
            s_iter.data[-1] += 1
        result = calc_tree(node.right, s_num, s_oper, s_iter)
    if len(s_num.data[sum(s_iter.data):]) == 2 and len(s_oper.data[sum(s_iter.data):]) == 1:
        while s_iter.data[-1] >= 0:
            x = s_num.pop()
            y = s_num.pop()
            o = s_oper.pop()
            
            result = calc(x, y, o)          
            s_num.push(result)                 
            s_iter.data[-1] -= 1
        s_iter.pop()
    return result


if __name__ == "__main__":
    #data = [10, 5, "-", 5, "*", 21, 7, "/", "+"]
    #data = [1, 3, "+", 2, 8, 1, "*", "+", "*", 10, 2, "-", "+"]
    #data = [11, 5, "-", 6, 2, "*", 7, "+", "*", 15, 5, "-", "+"]
    #data = [20, 2, "-", 5, 2, "-", 3, 9, 15, "+", "*", "+", "*", 15, 21, 7, "/", "-", "+"]
    data = [10, 4, "-", 3, 7, "+", 2, 9, 3, "-", "*", "*", 5, "-", "*", 15, 10, 2, "+", 5, "-", "-", "*"]
    print(data)
    head = construct_tree(data)
  
    s_num = Stack()
    s_oper = Stack()
    s_iter = Stack()
    s_iter.push(0)
    print(calc_tree(head, s_num, s_oper, s_iter))