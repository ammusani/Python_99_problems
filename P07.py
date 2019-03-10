#This program is 7th of the 99 problems in Python 
#It flattens the given nested list.
#Working function is flatIt

def flatIt(list, finList):
    for i in list:
        if type(i) == type(list):
            flatIt(i, finList)
        else:
            finList.append(i)

#test code, list hard code
list1 = [[1, 2, 3], 5, [1, 2, [4, 6, 7]]]
finList = []
flatIt(list1, finList)
print("Flatenned list = " + str(finList))
