# Sorting

- Sorting is the Process of Arranging the data in some Logical Order
- This Logical order may be Ascending and Descending in case of Numeric Vlaues or dictonary order in case of alphanumeric values

#### Two types of Sorting
- Internal Sorting
- External Sorting

#### Note
- Generally,when we run a Program,It is allocated some memory in the RAM
- In this memory,variables are formed
- The data which needs to be sorted,will exist in the RAM
- For example,The numbers which needs to be sorted are stored in this Variables
##### INTERNAL SORTING
- So,in our Program,we need to build some kinda Logic to arrange them,in a sorted Manner 
- In a definite memory of RAM,we sort the DATA
##### EXTERNAL SORTING 
- If the data is large,and is stored in Secondary Harddisk and it is not possible to bring it to the variable of the Program
- It is a challenge to sort this type of DATA in RAM,so it is brought in pieces to the program to perform sorting Techniques
- It is External Sorting

#### INTERNAL SORTING:
##### Bubble Sort:
- Bubble Sorting is very Simple and Easy to Understand to implement Sorting Technique
- Until inless explictingly said,sorting is Ascending Order
   - Ex: Let us sort 34,15,29,8  -->  A0 and A1 is compared -Swap --> A1 and A3 is compared -Swap --> Till end
   - For 4 elements,3 comparisons are done (N elements --> N-1 Rounds)
   - In Bubble Sort,Logic Starts with Comparison of First two elements and if the Left element is Greater than     Right Element,they Swap their Position
   - The Comparison is continued to the End of the Array
###### GENERAL STEPS: 
```python3

  nums = [5,3,8,6,7,2]
  def sort(nums):
    for i in 

  
  
```