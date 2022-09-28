#Program to calculate BMI using lists and different data types
#Author = Aditi Kharche
#Date = september 28,2022



height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
age = int(input("Enter the age: "))
#height = 150
#weight=50.2
bmi = weight/(height/100)**2
print("Your body mass index is",bmi)
if bmi <= 25:
    bmilist = [height,weight,age,"You are Healthy"]
    print("Height=" ,bmilist[0], "Weight=",bmilist[1],"Age is",bmilist[2])
    print("Result=",bmilist[3])
else:
    print("You are obese")
    