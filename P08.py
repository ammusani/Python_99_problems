#This is 8th program from 99 programs in Python
#This program eliminates consecutive duplicates
#working function is shortIt

def shortIt(list):
    lastEl = None
    finList = []
    for i in list:
        if i != lastEl:
            finList.append(i)
            lastEl = i

    return finList

#test code, list is hard coded
list1 = [1, 1, 1, 2, 2, 3, 3, 1]
finList = shortIt(list1)
print("Shortened list = " + str(finList))