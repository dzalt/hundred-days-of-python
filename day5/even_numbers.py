# Calculate even numbers 1 - 100

result = 0

for i in range(1, 101):
    if i % 2 == 0:
        result += i

# alt (using step)
# for i in range(2, 101, 2):
#     result += i

print(result)
