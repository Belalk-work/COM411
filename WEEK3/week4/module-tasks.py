#import random from built function
import random
#ask the user to enter a minimum number
print("Please enter the minimum value:")
min_value = int(input())        #in form of integer
#again ask user to enter a max number
print("Please enter the maximum value:")
max_value = int(input())            #for number, integer is used
#built function called random
random_number = random.randrange(min_value, max_value)

print(f"I am thinking of a number between {min_value} and {max_value}.")
print("guess what number it is?")
#while loop
while (True):
    print("enter a number:")
    guess = int(input())

    if guess == random_number:
        print("good guess, its correct!")
        break                       #break, determined the guessing number
    elif guess < random_number:
        print("Guess higher")
    else:
        print("Guess lower")

print("Game over!")


