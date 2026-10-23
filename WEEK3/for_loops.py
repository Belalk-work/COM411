#loop count
print("how far are we from the target?")

number_steps =int(input())
print()
for count in range (number_steps,0,-1):
    print(f"{count} , step is remaining")
print("we reached the target")

#range
print("what level of brightness is required?")
brightness_level =int(input())

for brightness_level in range(2,brightness_level+1 ,2):
    print(f"brightness_level : {'*'*brightness_level}")
print("too bright, we will be blind")







