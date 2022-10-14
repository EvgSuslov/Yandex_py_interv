 
list1 = list(input()) 
list2 = list(input()) 
list1.sort() 
list2.sort() 

position = 0 
matches = True 

while position < len(str1) and matches: 
    if list1[position]==list2[position]: 
        position = position + 1 
    else: 
        matches = False 

print((matches)) 
