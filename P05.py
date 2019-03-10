#This program is 5th of the 99 problems in Python 
#It reverses the list
#revList is the working function

def revList(list):
    size = len(list)
    finList = []
    for i in range(size - 1, -1, -1):
        finList.append(list[i])

    return finList

#test code, list is hard coded
list1 = [1, 43, 132, 41]
finList = revList(list1)
print("final list = " + str(finList))
