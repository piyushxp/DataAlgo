# Stack Data Structure:
- Stack is a linear data structure which follows a particular order in which the operations are performed. 
- The order may be LIFO(Last In First Out) or FILO(First In Last Out).
 ++
## Let's Code a Stack
- Python’s buil-in data structure list can be used as a stack

```python

stack = [] 
  
# append() function to push 
# element in the stack 
stack.append('a') 
stack.append('b') 
stack.append('c') 
  
print('Initial stack') 
print(stack) 
  
# pop() function to pop 
# element from stack in  
# LIFO order 
print('\nElements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 
  
print('\nStack after elements are popped:') 
print(stack) 
```