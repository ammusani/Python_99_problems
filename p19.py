#This is the 19th program in 99 programs in Python
#This returns list rotated to left by n digits
#working function rotate_it_left

def rotate_it_left(list, n):
    if n >= 0:
        for i in range(n):
            l = list.pop(0)
            list.append(l)
    else:
        n *= -1
        for i in range(n):
            l = list.pop()
            list.insert(0, l)
            
#test code, list and n are hard coded
n = -3
list = ["a", "b", "c", "d", "e", "f", "g", "h"]
rotate_it_left(list, n)
print(list)