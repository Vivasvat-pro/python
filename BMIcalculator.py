height = float(input("enter you height in cm: "))
weight = float(input("enter your weight in kg: "))
BMI = weight / (height/100)**2
print("your BMI is:", BMI)
if BMI <= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are heallthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severlly over weight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severlly obese")