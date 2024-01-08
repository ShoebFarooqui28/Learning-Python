#break
while True :
    name = input("Enter Your Name : ")
    if name != "" : 
        break 

#continue    
phoneNumber = "123-456-7890"

for i in phoneNumber :
    if i == "-" :
        continue    
    print(i, end="")

print()

#pass 
for i in range(1, 20) :
    if i == 6 :
        pass
    else :
        print(i)
