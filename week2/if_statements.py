#task1
print("what type of book is this?")
book_type =input()
if book_type == "adventure":
     print("I like adventure books!")
print("finished reading book.")
#equal operator is used to evaluate the expression of the book activity 2 if...else statement
from turtle import left

print("is the first number is bigger than the second number?")
first_number = 5
second_number =1
if first_number > second_number:
     print("first is bigger")
# else:
     print("first is equal or smaller")
print("done")
#tasks
print("please enter your activity")
activity =input ()

if activity == "9":
     print("performing activity is great")
else:
     print("the activity isn't correct")
print("activity completed")

#elif
print("which direction the robot should move up, down, left, right?")
direction = input()
if direction =="up":
     print("the robot going upward direction")
elif direction =="down":
     print("the robot going downward direction")
elif direction =="left":
     print("the robot going left direction")
elif direction =="right":
     print("the robot going right direction")
else:
     print("the robot is lost")
print("completed the task")
#modulo
print("enter a whole number")
number =int(input())
if number % 2 == 0:
    print(f"the number {number} is even number")
else:
    print(f"the number {number} is odd number")