temp = int(input("What's the temperature right now?\n"))

if temp <= 30 and temp >= 15 :
    print("It's Moderate out there!")

elif temp <= 0 and temp >= -15 :
    print("It's Freezing out there!")
    
elif temp > 30 : 
    print("It's Extremly Hot out there!")

else :
    print("Its Breezy out there!")