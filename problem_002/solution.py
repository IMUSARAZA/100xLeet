import math



def simpleArraySum(ar):

    sum = 0

    for i in range(len(ar)):
        sum = ar[i] + sum

    return sum



print(simpleArraySum([1,2,3,4,10,11]))

