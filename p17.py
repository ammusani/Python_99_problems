#This is the 17th program in 99 programs in Python
#This splits the list into two parts, 1st size specified by n
#working function split_it

def split_it(list, n):
    list2 = []
    j = len(list)
    for i in range(n):
        list2.append(list[0])
        list.pop(0)
        if i == j - 1:
            break
    return list2

#test code, list and n hard coded

n = 4
list = [1, 5, 3, 5, 88, 4, 3]
list2 = split_it(list, n)
print(list2)
print(list)