person = {'name':'reza','last_name':'keshavarz','age':34}

#print(person["salary"])

try:
    print(person["salary"])
except:
    print("does not exist")


print(int(input("enter the salary:\n")))
