# Don't change the code below
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# Don't change the code above

# Write your code below this line

bmi = round(weight / height ** 2)

result = ""

if bmi < 18.5:
    result = "underweight"
elif bmi < 25:
    result = "normal weight"
elif bmi < 30:
    result = "slightly overweight"
elif bmi < 35:
    result = "obese"
else:
    result = "clinically obese"

print(f"Your BMI is {bmi}, you are {result}.")
