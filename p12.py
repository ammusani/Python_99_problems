#This is the 11th program in 99 programs in Python
#This program creates a decoded list from the encoded list created in previous programme
# decode_it is the working function

def decode_it(list):
    fin_list = []
    
    for i in list:
        if type(i) == tuple:
            j = i[0]
            k = i[1]
            for l in range(j):
                fin_list.append(k)
        
        else:
            fin_list.append(i)
    
    return fin_list



#test code, list is hard coded

list = [(5, "a"), (2, "b"), (4, "c"), (7, "d")]

list = decode_it(list)

print(list)