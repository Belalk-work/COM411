# build in functions
print("the program started")
print("enter a standard character")
character = input()
if len(character) == 1:
    print(f"the ASCII code for {character} is {ord(character)}")

else:
    print("wrong, enter the only charactor again")
print("end of the program")