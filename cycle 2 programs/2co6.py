#count the number of characters in a string
str=input("Enter a string:")
c=0
for i in str:
    if i=="":
        continue
    else:
        c+=1
print(c)        
