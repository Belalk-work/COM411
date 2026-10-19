#task 1, while loop
print("how many apples shall i remove?")
number_to_remove = int(input())

removed_apple = 0
print()
while removed_apple<number_to_remove:
    removed_apple += 1
    print("removed_apple")

#task2
print("how many obstacles i must avoid?")
obstacle_to_avoid= int(input())
avoided_obstacle = 0
print()
while avoided_obstacle<obstacle_to_avoid:
    print("avoiding...", end="")
    avoided_obstacle = avoided_obstacle + 1
    print(f"done! {avoided_obstacle} avoided obstacle")

