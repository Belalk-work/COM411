print("what type of adventure us this?")
adventure_type=input()
if (adventure_type == "scary") or (adventure_type == 'short'):
    print("entering the dark forest!")
elif    (adventure_type == 'safe') or (adventure_type == 'long'):
    print("tasking the safe route")

else:
    print("you don't know what to do!")
# logical and operator.
print("what did i hear?")
hear =input()
print("what did i see?")
see=input()
if (hear == "grrr") and (see== "two red eye"):
    print("there is a scary creature, we should get out here")
else:
    print("i am little scared but i carry on!")