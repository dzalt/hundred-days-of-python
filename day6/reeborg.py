# # Link: https://reeborg.ca/reeborg.html

##################################################
# # Lesson 1: Alone - Draw a Square
##################################################

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# turn_left()
# move()
# turn_right()
# move()
# turn_right()
# move()
# turn_right()
# move()

##################################################
# # Lesson 2: Hurdle 1
##################################################

# def jump():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     jump()

##################################################
# # Lesson 3: Hurdle 3
##################################################

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

##################################################
# # Lesson 4: Hurdle 4
##################################################

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif wall_in_front():
#         turn_left()
#     else:
#         move()

##################################################
# # Lesson 5: Maze
##################################################

# # Follow along the right edge of the maze
# # Turning right if it can
# # Going straight ahead if it can’t turn right
# # Turning left as a last resort.

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
