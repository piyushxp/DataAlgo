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


s = Stack()
# pushing A and B
s.push("A")
s.push("B")
print(s.get_stack())
# pushing C
s.push("C")
print(s.get_stack())
# popping,removing 
s.pop()
print(s.get_stack())
print(s.isEmpty()) #Check if stack is Empty
