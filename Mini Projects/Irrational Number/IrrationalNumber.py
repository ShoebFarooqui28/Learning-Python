import math
num = float(input("Enter The Number: "))

def test(num):
    numSqrt = math.sqrt(num)
    
    if numSqrt == int(numSqrt):
        return f"The square root of {num} is Rational! : {int(numSqrt)}"
    else:
        return f"The square root of {num} is Irrational! : {numSqrt}"


result = test(num)
print(result)