#5 functions

#display box fuction
def display_box(word):
    print("*" * (len(word) + 4))
    print("* " + word + " *")
    print("*" * (len(word) + 4))

#display lower case function
def display_lower(word):
    print(word.lower())

#display upper case function
def display_upper(word):
    print(word.upper())
#display mirrored function
def display_mirrored(word):
    print(word + " | " + word[::-1])

#display repeat function
def repeat_word(word):
    times = int(input("How many times would you like to display the word? "))
#loop function
    for i in range(times):
        if i % 2 == 0:
            print(word.upper())
        else:
            print(word.lower())


def run_program():
    word = input("Enter a word: ")
#outcome
    print("\nChoose an option:")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    option = int(input("Enter your option (1-5): "))

    if option == 1:
        display_box(word)
    elif option == 2:
        display_lower(word)
    elif option == 3:
        display_upper(word)
    elif option == 4:
        display_mirrored(word)
    elif option == 5:
        repeat_word(word)
    else:
        print("Invalid, please entre between 1 and 5.")


# call to function
run_program()