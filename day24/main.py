with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for i in names:
    new_name = i.strip()
    with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as file:
        file.write(letter.replace("[name]", new_name))
