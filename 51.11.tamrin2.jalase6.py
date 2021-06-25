getSum = [1, 2, 3, 4, 5]

def getSum(piece):
    if len(piece)==0:
        return 0
    else:
        return piece[0] + getSum(piece[1:])
print(getSum([1, 3, 4, 2, 5]))
