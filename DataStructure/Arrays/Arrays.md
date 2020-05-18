# Arrays:

> A collection of elements or values each identified by an array index.
--> Index starts at 0,generally
-->Because of indexes,random access is possible

1.Arrays are data structure that helps to store Data of the Same type.
2.Array can have as many dimensions as we want,one or two dimensional arrays are quite popular
3.Storing a Matrix --> 2 dimensional Array
4.Dynamic Array --> When the size of the Array is changing dynamically
5.Applications: lookup tables/hashtables ,heaps  --> Several ADT uses Arrays as Data-structure

## Advantages:
1.We can use Random Access Because of the Keys: getItem(int index) --> returns the value very Fast ==> O(1)
2.Very easy to implement and use
3.Very fast Data structure
4.We should use arrays in Applications when we want to add Items over and over again and we want to take items with given index


## Disadvantages:
1.We have to know the Size of array at compile Time,So it is not a Dynamic Data structure
2.If it is full : We have to create a Bigger Array and have to Copy the Values one by one ,i,e reconstructing an array ==> O(n)
3.It is not able to store items with different types