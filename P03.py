#This is the 2nd program of 99 problems in Python
#It returns the kth element in the list, if k is greater than size, returns an error
#kthEl is the working funtion


def kthEl(k, list):
    error = "N/A, k out of bound"
    if k >= len(list):
        return error
    else:
        return list[k]

#test code, list is hard coded
list1 = [1, 43, 132, 41]
k = 2
print("kth element = " + str(kthEl(k, list1)))
