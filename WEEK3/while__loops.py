#iterate through letter
print("enter the phrase")
phrase = input()
hello = 0 #
while hello < len(phrase):
    print(" wow ", end="")
    hello = hello + 1





# repetitive steps

print("calculating the sum of the first 100 numbers...!")
numbers=1

total = 0
while numbers <= 100:
    total = total + numbers
    numbers = numbers + 1
    print(f"......done, the answer is: {total}")



#another task, ask user to enter a number
print("how many numbers should i sum up?")
the_number=int(input())
the_sum=0
print()
while the_sum < the_number:
    print(f"put a number {the_sum} of {the_number}")
    number = int(input())
    total = total+ the_number
    the_sum = the_sum + 1
    print(f"the answer is {total}")














