#adding more functions

def display_ladder(steps):
    for steps in range(steps):
        print("|  |")
        print("***")
        print("|  |")

#another function
def create_ladder():
    print("enter the number of steps") #display message
    steps = int(input())
    display_ladder(steps)

#call to function
create_ladder()
