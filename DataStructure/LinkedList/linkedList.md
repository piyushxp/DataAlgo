# Linked List:

Every Linked lIst consist of Nodes
- Every Node has 2 Components
  - Data
  - Next
- Data stores data nd Next points to another Node
- The start of the List is called as HEad,This is a pointer
- If we want to iterate through the list,the Head Pointer has to move along the List,that is why Accessing an element in Linkedlist in O(n)
- "NULL" depicts the end of the List

## Array V/s Linked List:
- 1. in Array  => Insertion/Deletion --> O(n)  2.Access an element --> O(1)
- 2. in Linked Lis =>Insertion/Deletion --> O(1)  2.Access an element --> O(n)
- Array has contiguous Memory(so access is O(n)) while LinkedList doesn't.


## LInked lIst --> Insertion:
### Append - single Linked List:

```python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self)


```
