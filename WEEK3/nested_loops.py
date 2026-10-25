#nested loops
print("how many row you want?")
row = int(input())
print("how many columns you want?")
column = int(input())
for row in range(0, row, 1):
    for column in range(0, column, 1):
        print("❀", end="")
    print()

print("job done")
