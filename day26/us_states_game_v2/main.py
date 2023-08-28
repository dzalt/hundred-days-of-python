import turtle
import pandas

# set screen
screen = turtle.Screen()
screen.title("US States Game")

# add image as background
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# main game
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed = []

while len(guessed) < 50:
    guess = screen.textinput(title=f"{len(guessed)}/50 States Correct", 
                             prompt="What's another state's name:").title()

    if guess in states and guess not in guessed:
        guessed.append(guess)
        display_name = turtle.Turtle()
        display_name.hideturtle()   # to hid turtle icon
        display_name.penup()        # to remove line trail
        state_name = data[data.state == guess] # pick row
        display_name.goto(int(state_name.x), int(state_name.y))
        display_name.write(guess)

    elif guess == "Exit":
        missing = [i for i in states if i not in guessed]
        # missing = []
        # for i in states:
        #     if i not in guessed:
        #         missing.append(i)
        
        homework = pandas.DataFrame(missing)
        homework.to_csv("states_to_learn.csv")
        break
    
# print(guessed)
# print(missing)
