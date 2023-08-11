# If the bill was $150.00, split between 5 people, with 12% tip. 
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.
# Write your code below this line

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? "))
person = int(input("How many people to split the bill? "))

result = (bill/person) * (tip / 100 + 1)

# result = round(result, 2)
result = "{:.2f}".format(result)

# if result has zero (12.00)
# with round -> 12.0
# with format -> 12.00

print(f"Each person should pay: {result}")