height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
age = int(input("Enter the age: "))
#height = 150
#weight=50.2
bmi = weight/(height/100)**2
print("Your body mass index is",bmi)
if bmi <= 25:
        bmidict = {
                    "weight": weight,
                    "Height": height,
                    "age": age,
                    "Result": "You are Healthy"
                  }
        print(bmidict["Result"])
else:
        print("You are obese")