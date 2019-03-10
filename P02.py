#This is the 2nd program of 99 problems in Python
#It returns the second last element in the list
#secLastEl is the working funtion

def secLastEl(list):
    return list[-2]

#test code, list is hard coded
list1 = [1, 43, 132, 41]
print("second last element = " + str(secLastEl(list1)))
