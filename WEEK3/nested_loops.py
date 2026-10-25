#nested loops in decision
print("enter a sequence")
sequence = input()
print("enter marker")
marker = input()
marker1_position = -1
marker2_position = -1
for position in range(0, len(sequence), 1):

    if sequence == marker:
        if (marker1_position == -1):
            marker1_position = position
        else:
            marker2_position = position

print(f"the distance is {marker2_position - marker1_position-1}")







