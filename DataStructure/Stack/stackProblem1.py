"""
Reversing a String using a Stack
input_str = "Hello"
result should be "olleH"


"""

class Stack():
    def __init__(self):
        self.items =[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items ==[]
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
    def get_stack(self):
        return self.items
    
def reverse_string(stack,input_str):
    # Loop through the string and push contents 
    for i in range(len(input_str)):
            stack.push(input_str[i])
    rev_str= ""
    while not stack.isEmpty():
            rev_str =rev_str+ stack.pop()
    return rev_str

input_str = "Hello"
stack = Stack()


print(reverse_string(stack,input_str))
    
