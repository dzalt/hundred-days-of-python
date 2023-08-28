# create a list that contains numbers that are both in list1 and list2

with open("file1.txt") as file:
    list1 = file.readlines()

with open("file2.txt") as file:
    list2 = file.readlines()

# print(list1) 
# ['3\n', '6\n', ... ]
# int(n) will automatically strip new lines (\n)

result = [int(n) for n in list1 if n in list2]

print(result)