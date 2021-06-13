# tamrin 5
# revers kardan list

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def revers(num):
    if(len(num) == 1):
        return num
    return revers(num[1:]) + num[0:1]

print(revers(num))
