"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))  -->edge case

"""

# Solution

from stack import Stack

def isParenBalanced(parenString):
    s = Stack()
    is_balanced = True
    index = 0

    while index<len(parenString) and is_balanced:
        paren = paren_string[index]