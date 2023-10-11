'''
Give it a try on reeborg.ca and have some fun bruh ;-)
'''
def turn_right():
    for i in range(0,3):
        turn_left()
def move_f():
    while front_is_clear():
        if not at_goal():
            move()
        if at_goal():
            done()
        if not wall_on_right():
            turn_right()
    while wall_in_front():
        turn_left()
def n_a_g():
    while not at_goal():
        move_f()
n_a_g()