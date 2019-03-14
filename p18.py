#This is the 18th program in 99 programs in Python
#This returns slicec of the list specified by n, m
#working function slice_it

def slice_it(list, n, m):
    slicedList = []
    for i in range(n - 1, m):
        slicedList.append(list[i])
    return slicedList

#test code, list n, m hard coded

n = 3
m = 7
list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
sliced_list = slice_it(list, n, m)
print(sliced_list)
