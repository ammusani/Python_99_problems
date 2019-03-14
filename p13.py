#This is the 13th program in 99 programs in Python
#This is different version of the program number 10, here addition and removal done at the run-time
#working function superList4

def superList4(list):
    lastEl = None
    finList = []
    for i in list:
        if i == lastEl:
            l = finList.pop()
            j = l[0]
            l = (j + 1, lastEl)
            finList.append(l)
        else:
            finList.append((1, i))
            lastEl = i

    return finList

#test code, list is hard coded

list1 = ["a", "a", "a", "b", "b", "c", "c", "a"]
finList = superList4(list1)
print("Super list = " + str(finList))