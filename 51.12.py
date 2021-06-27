getSum([1, 2, 3, 4, 5]) 

def getSum(iterable):
    if not iterable:
        return 0  # End of recursion
    else:
        return iterable[0] + getSum(iterable[1:])
