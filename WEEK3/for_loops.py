

# reverse loop
print("what phrase do you want to write?")
phrase= input()
print("\n reversing\n")
print("the phrase;", end="")

for position in range(len(phrase)-1, -1, -1):
    print(phrase[position] , end="")