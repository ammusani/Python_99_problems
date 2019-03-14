#This is the 14th program in 99 programs in Python
#This creates a duplicate of each element in the list
#working function duplicate_it

def duplicate_it(list):
    finList = []
    
    for i in list:
        finList.append(i)
        finList.append(i)
    
    return finList


#test code, list is hard coded

list1 = ["a", "c", "e", "p"]
finList = duplicate_it(list1)
print(finList)