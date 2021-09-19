#BMI calculator

name = input('name')
height_feet = int(input('height in feet'))
height_inches = int(input('height in inches'))
height_feet_inches = (height_feet * 12) + height_inches
weight_lbs = int(input('weight in pounds'))
bmi = ((weight_lbs/height_feet_inches ** 2) * 703)

print(name)

if bmi >= 25:
    print("You Are Overweight")
elif bmi <= 18.5:
    print("You Are Underweight")
else:
    print("Your bmi is normal")
print("Your BMI is:", end=' ')
print(round(bmi, 2))
