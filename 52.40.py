list = [1,3,2,4,5,3,6,1]

def sort(list):
    if len(list) < 2:
        return list

    a_1 = list[0]
    a_2 = []
    a_0 = []
    for i in list[1:]:
        if i > a_1:
            a_2.append(i)
        else:
            a_0.append(i)

    return sort(a_0) + [a_1] + sort(a_2)

print(sort(list))
