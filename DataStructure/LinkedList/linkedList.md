# Linked List:

#### Every Linked lIst consist of Nodes
- Every Node has 2 Components
  - Data
  - Next
- Data stores data and Next points to another Node
- The start of the List is called as HEad,This is a pointer
- If we want to iterate through the list,the Head Pointer has to move along the List,that is why Accessing an element in Linkedlist in O(n)
- "NULL" depicts the end of the List

## Array V/s Linked List:
- 1. in Array  
  - Insertion/Deletion --> O(n)  
  - 2.Access an element --> O(1)
- 2. in Linked Lis 
  - Insertion/Deletion --> O(1) 
  -  2.Access an element --> O(n)
- Array has contiguous Memory(so access is O(n)) while LinkedList doesn't.


## Linked-List:
- Prepend - O(1) --> add at beginning
- Append - O(1)   --> add at end
- Lookup - O(n)  --> traversal
- Insert - O(n)  --> One by one ,to Insert
- Delete - O(n)   --> one by one, to delete

## LInked list - Insertion:
### Append - single Linked List:

```python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self)


```

## Javascript Glance:
- Pseudocode in JS: 
  ```js
  const basket = ['apples','grapes','pears']

  Linked-List : apples --> grapes --> pears

  apples
  7867  --> grapes
            6767  --> pears
                      7868 --> null
  ```

- Why Linked-List are better than other DS?
 Try [visualalgo.net](https://visualalgo.net) -- Create,Insert,remove Nodes 


 ### What is Pointer:
 - Pointers are simply variables that store the address of an object. 
 - It is simply a reference
 
 #### Demo:
 ```js
 
 10--> 5 --> 16

//Visualize
 let myLinkedList = {
   head:{
     value: 10
     next:{
       value: 5,
       next:{
         value:16,
         next:null
       }
     }
   }
 }

//LETS BUILD
 class LinkedList{
   constructor(value)
   this.head = {
     value:value,
     next: null
   }
   this.tail =  this.head
   this.length = 1

//APPEND
   append(value){
     const newNode= {
       value:value,
       next:null
     }
     this.tail.next = newNode
     this.tail = newNode
     this.length++
     return this
   }
 }

 const myLinkedList = new LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)

/*

LinkedList {
  head: { value: 10, next: { value: 5, next: [Object] } },
  tail: { value: 16, next: null },
  length: 3
}
*/
 
 ```