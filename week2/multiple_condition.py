print("what type of adventure us this?")
adventure_type=input()
if (adventure_type == "scary") or (adventure_type == 'short'):
    print("entering the dark forest!")
elif    (adventure_type == 'safe') or (adventure_type == 'long'):
    print("tasking the safe route")

else:
    print("you don't know what to do!")
