height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
#height = 150
#weight=50
bmi = weight/(height/100)**2
print("Your body mass index is",bmi)
if bmi <= 25:
        bmidict = {
                    "weight": weight,
                    "Height": height
                  }
        print(bmidict)
        print("You are Healthy")
else:
        print("You are obese")