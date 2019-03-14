#This is the 16th program in 99 programs in Python
#This drops nth element of the list
#working function drop_nth_list

def drop_nth_list(list, n):
    finList = []
    for i in range(len(list)):
        if i % n != n - 1:
            finList.append(list[i])

    return finList

#test code, list hard coded
n = 4
list = [1, 3, 4, 5, 6, 6, 7, 9, 2, 3, 4, 6, 9]
list = drop_nth_list(list, n)
print(list)
