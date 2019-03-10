#This program is 6th of the 99 problems in Python 
#It finds whether the given list is a palindrome or not. 
#working function isPalindrome

def isPalindrome(list):
    flag = 1
    size = len(list)
    halfSize = int(size/2)
    for i in range(0, halfSize):
        if list[i] != list[size - i - 1]:
            flag = 0
            break
    return flag

#test code, list hard coded
list1 = [1, 2, 3, 3, 4, 1]
if isPalindrome(list1):
    print("Yes")
else:
    print("No")