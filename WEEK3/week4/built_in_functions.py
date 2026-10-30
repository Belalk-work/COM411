#using abs,range, chr
print("the program started")
print("enter your ASCII code")
code = int(input())
if code >=32 and code <= 126:
    print(f"the character represented BY ASCII code is {code} is {chr(code)}")

else:
    print("invalid ASCII code")
print("end of the program")