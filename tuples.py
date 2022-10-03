# Program to show the use of tuple using whether number is even or odd.
# Author = Aditi Kharche
# Date= October3,2022


num1 = int(input("Enter a number1: "))
mod = num1 % 2
num2 = int(input("Enter a number2: "))
mod2 = num2 % 2
num3 = int(input("Enter a number1: "))
mod3 = num3 % 2
mytuple = (num1,num2,num3)
if mod > 0:
    print(mytuple[0],"an odd number.")
else:
    print(mytuple[0],"an even number.")
if mod2 > 0:
    print(mytuple[1],"an odd number.")
else:
    print(mytuple[1],"an even number.")
if mod3 > 0:
    print(mytuple[2],"an odd number.")
else:
    print(mytuple[2],"an even number.")