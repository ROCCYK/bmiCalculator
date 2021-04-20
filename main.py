#BMI calculator

name = "himal patel"
height_feet = 5
height_inches = 11
height_feet_inches = (height_feet * 12) + height_inches
weight_lbs = 145
bmi = ((weight_lbs/height_feet_inches ** 2) * 703)

print(name)

if bmi >= 25:
    print("You Are Overweight")
elif bmi <= 18.5:
    print("You Are Underweight")
else:
    print("Your bmi is normal")
print("Your BMI is:")
print(round(bmi, 2))
