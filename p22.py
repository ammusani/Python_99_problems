#This is the 22nd program in 99 programs in Python
#This returns a list with elements in range n, m
#working function genListNtoM

def genListNtoM(n, m):
    list = []
    for i in range(n, m + 1):
        list.append(i)
    return list

#test code, n and m are hardcoded

n = 4
m = 9
list = genListNtoM(n, m)
print(list)