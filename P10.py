#This is the 10th program in 99 programs in Python
#This is extension of the last program, instead of storing the complete list your store the element and its size
#superList2 is the working function

def superList2(list):
    lastEl = None
    count = 0
    finList = []
    for i in list:
        if i == lastEl:
            count += 1
        else:
            if count != 0:
                finList.append((count, lastEl))
                count = 0
            count = 1
            lastEl = i

    finList.append((count, lastEl))
    return finList

#test code, list is hard coded
list1 = ["a", "a", "a", "b", "b", "c", "c", "a"]
finList = superList2(list1)
print("Super list = " + str(finList))