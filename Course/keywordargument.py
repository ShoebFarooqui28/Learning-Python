def details(first, middle, last):
    print("Your Full Name is : "+ first, middle, last)


firstName = input("Enter your First Name : ")
middleName = input("Enter your Middle Name : ")
lastName = input("Enter your Last Name : ")

details(last=lastName, middle=middleName, first=firstName)
