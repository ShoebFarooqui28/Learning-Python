def hello(fName, lName, age):  # name is the parameter of the argument
    print("Hello")
    print("You are " + fName,lName)
    print("You are " + str(age) + " Yrs Old")


firstName = input("Enter Your First Name : ")
lastName = input("Enter Your Last Name : ")
age = input("Enter your Age : ")
hello(firstName, lastName, age)  # taking name as an argument
