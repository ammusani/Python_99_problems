#This is the 21st program in 99 programs in Python
#This inserts element y at nth position
#working function insertatN

def insertatN(list, n, y):
    list.insert(n - 1, y)

#test code, hard coded n, y, list

n = 3
y = 99
list = [1, 54, 67, 34, 123]
insertatN(list, n, y)
print(list)