#defined function with 2 parameter
def climb_ladder(num_steps_remaining, crossed_steps):
    if num_steps_remaining > crossed_steps:
#display message
        print("keep going")
    else:
        print("we are almost there")
#call to function
climb_ladder(2, 3)
climb_ladder(5, 2)
climb_ladder(4, 3)

