#This is the 9th program in 99 problems in Python
#Program creates a super list in which all the duplicate consecutive elements are in a same list
#superList is the working function

def superList(list):
    lastEl = None
    sudoList = []
    finList = []
    for i in list:
        if i == lastEl:
            sudoList.append(i)
        else:
            if len(sudoList) != 0:
                finList.append(sudoList)
                sudoList = []
            sudoList.append(i)
            lastEl = i

    finList.append(sudoList)
    return finList

#test code, list is hard coded
list1 = [1, 1, 1, 2, 2, 3, 3, 1]
finList = superList(list1)
print("Super list = " + str(finList))