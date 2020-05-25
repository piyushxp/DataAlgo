def getSquaredNumbers(numbers):
    squaredNumbers=[]
    for n in numbers:
        squaredNumbers.append(n*n)
    return squaredNumbers

numbers = [2,3,4,5]
getSquaredNumbers(numbers)
# returns [4,9,16,25]

"""
Order of 0(n)
"""