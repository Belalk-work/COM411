#task2
print("how many obstacles i must avoid?")
obstacle_to_avoid= int(input())
avoided_obstacle = 0
print()
while avoided_obstacle<obstacle_to_avoid:
    print("avoiding...", end="")
    avoided_obstacle = avoided_obstacle + 1
    print(f"done! {avoided_obstacle} avoided obstacle")

