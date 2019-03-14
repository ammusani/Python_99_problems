#This is the 20th program in 99 programs in Python
#This returns list and kth element which is removed from the list
#working function removeKth

def removeKth(list, k):
    if k >= len(list):
        return "Error, out of bound", -1
    kth = list.pop(k)
    return list, kth

#test code, k and list are hard coded

k = 4
list = ["asa", "afdf", "fafsa", "afwq", "fdfsd"]
list, kth = removeKth(list, k)
print(list)
print(kth)
