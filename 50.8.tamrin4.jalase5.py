list = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

#1.for
#2.while



def sum_of_list(l,n):
  if n == 0:
    return l[n];
  return l[n] + sum_of_list(l,n-1)


print( "The sum of list is", sum_of_list(list,len(list)-1))




#-------------------------

#dorost


def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

print( "The sum of list is", sum_of_list(list))

#-----------------------

#ghalat

#for i in range(1,11):

#sum = 0
#if i in a:
#    sum = sum + i
#output = {"sum":sum}
#print(output)



#----------------------
#def factorial(a):
#    if a == 0:
#        return 1
#    return a * factorial(a - 1)

#print(factorial(10))

#--------------------------

#for a in range(1,11):
#    print(a)

#--------------------------
#for index,adad in enumerate(a):
#    if adad == 0:
#        return 1
#    print( a + (a + 1))
#---------------------------
