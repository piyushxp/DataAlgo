"""
Use a stack to check whether or not a string
has balanced usage of parenthesis/bracket
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))  -->edge case

"""

# Solution

from stack import Stack

def isMatch(p1,p2):
    return True if p1+p2 in ["()","[]","{}"] else False

def isBracBalanced(bracString):
    s = Stack()
    isBalanced = True
    index = 0

    while index<len(parenString) and isBalanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.isEmpty():
                isBalanced=False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    isBalanced=False
        index = index+1

    if s.isEmpty() and isBalanced:
        return True
    else: