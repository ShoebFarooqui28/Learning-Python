rows = int(input("Enter Rows : "))
cols = int(input("Enter Columns : "))
sym = input("Enter Symbol to use : ")

for i in range(rows) :
    for j in range(cols) :
        print(sym, end="")
    print()        
        