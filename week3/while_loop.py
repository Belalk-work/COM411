#while loop
print("how many apples shall i remove?")
number_to_remove = int(input())

removed_apple = 0
print()

while removed_apple < number_to_remove:
    removed_apple += 1                  #to avoid of endless repetition

    print("removed apple")