#build in function
def directions():
    direction = ["move forward" "move backward", "turn left", "turn right"]
    return direction
def run():
    if __name__== "__main__":
        print(directions())
run()
#task2 build in function

def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3,
        "Move Right", 1]
    return path


def run():
    print("Moving...")
    path = movements()
#the outcomes
    print(f"{path[0]} for {path[1]} steps")
    print(f"{path[2]} for {path[3]} steps")
    print(f"{path[4]} for {path[5]} steps")
    print(f"{path[6]} for {path[7]} steps")


if __name__ == "__main__":
    run()


