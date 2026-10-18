#nested-decision in decision
print("what cover_type do the book have?")
cover_type= input()
if cover_type == "soft":
    print("is the book the perfect-choice?")
perfect_choice= input()
if perfect_choice== "yes":
    print("hooray,soft cover books are affordable")
else:
    print("hard book covers are expensive")
