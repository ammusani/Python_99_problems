#This is the 11th program in 99 programs in Python
#This is extension of the last program, instead of storing the complete list you store the element and its size as new entries only for elements with more than one copies
#superList3 is the working function

def superList3(list):
    lastEl = None
    count = 0
    finList = []
    for i in list:
        if i == lastEl:
            count += 1
        else:
            if count != 0:
                if count > 1:
                    finList.append((count, lastEl))
                else:
                    finList.append(lastEl)
                count = 0
            count = 1
            lastEl = i

    if count > 1:
        finList.append((count, lastEl))
    else:
        finList.append(lastEl)
    return finList

#test code, list is hard coded
list1 = ["a", "a", "a", "b", "b", "c", "c", "a"]
finList = superList3(list1)
print("Super list = " + str(finList))
