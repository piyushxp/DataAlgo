"""

Use a STack Dats Structure to convert Integer values to Binary
Example: 242
242/2 = 121 ==> remiander 0
121/2 =60  ===> remiander 1
60/2 = 30  ==> remiander 0
so on

11110010  ==> check it by int("11110010",2)  gives 242
"""

# Solution
# Let's import stack
from stack import Stack

def divBy2(intNum):
    s= Stack()

    while intNum>0:
        remainder = intNum%2
        s.push(remainder)
        intNum=intNum//2
    
    binNum = ""
    while not s.isEmpty():
        binNum = binNum+ str(s.pop())
    return binNum
print(divBy2(242))
    