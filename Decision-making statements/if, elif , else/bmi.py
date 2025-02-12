""""

Metric units: BMI = weight (kg) / [height (m)]^2

Underweight>>Below 18.5
Healthy weight>>18.5 to 24.9
Overweight>>25.0 to 29.9
Obesity>>30.0 or greater
Severe obesity>>40 or over



"""

weight_kg = float(input("enter your weight in kg: "))

height_m = float(input("Enter your height in m: "))

bmi = weight_kg / (height_m ** 2)

print(f" you a BMI of {bmi}")

if bmi > 0 and bmi < 18.5:

    print("You are underweight")

elif bmi > 18.5 and bmi < 25:

    print("You are at an healthy weight")

elif bmi > 25 and bmi <30:

    print("You are overweight")

elif bmi > 30 and bmi < 40:

    print("You are Obese")

else:

    print("You are extremely Obese")