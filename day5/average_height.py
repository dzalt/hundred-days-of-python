# Don't change the code below
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Don't change the code above

# Write your code below this row

# without sum and len
student = 0
total = 0

for height in student_heights:
    student += 1
    total += height

# with sum and len
# student = len(student_heights)
# total = sum(student_heights)

print(round(total/student))

# 156 178 165 171 187
# 171