#This is the 15th program in 99 programs in Python
#This creates a duplicate of each element n times in the list
#working function duplicate_it_n_times

def duplicate_it_n_times(list, n):
    finList = []
    
    for i in list:
        for j in range(n):
            finList.append(i)
    
    return finList


#test code, list is hard coded

list1 = ["a", "c", "e", "p"]
finList = duplicate_it_n_times(list1, 4)
print(finList)