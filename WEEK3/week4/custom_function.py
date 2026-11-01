#return function in function
#first function
def sum_weights(person_weight, inventory_weight):
    total_weight = person_weight + inventory_weight
    return total_weight
#second function
def calc_avg_weight(person_weight, inventory_weight):
    avg_weight = sum_weights (person_weight + inventory_weight) / 2
    return avg_weight
#3rd function
def run():
    person_weight = float(input("Enter person weight: "))
    inventory_weight = float(input("Enter inventory weight: "))
    print("do you like to calculate( sum or avg)?")
    choice = input("Enter choice: ")
    #using if statement
    if choice == "sum":
        answer = sum_weights(person_weight, inventory_weight)
        print(f"the sum of wights is {answer:.2f}")
    elif choice == "average":
        answer = calc_avg_weight(person_weight, inventory_weight)
        print(f"the average weight is {answer:.2f}")
    else:
        print("Please enter a valid choice")


#call to function
run()

