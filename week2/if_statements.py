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
    #comparison operators
print("enter the first_number")
first_number =int(input())
first_number =7
print("enter the second_number")
second_number =int(input())
second_number =3
if first_number > second_number:
    print("the first_number is a biggest number")
elif first_number < second_number:
    print("the second_number is a biggest number")
else:
    print("the two numbers are equals")

#count up numbers whether its even or odd
print("enter the first whole number")
first_number =int(input())
first_number =2
print("enter the second whole number")
second_number =int(input())
second_number =4
print("enter the third whole number")
third_number =int(input())
third_number =5
even_number =0
odd_number = 0
if number % 2 ==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if second_number % 2 ==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1
if third_number % 2 ==0:
    even_number = even_number + 1
else:
    odd_number = odd_number + 1

    print(f"there are {even_number} even numbers and {odd_number}is odd number")

print("end of this section")
