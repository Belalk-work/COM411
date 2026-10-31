#defined function with parameter and loops
def cross_bridge(steps):
    for step in range(steps):
        print("crossed step")
    if steps <= 5:
           print("keep going")
    else:
        print("the bridge is collapsing!!!")
#call to functions
cross_bridge(3)
cross_bridge(7)