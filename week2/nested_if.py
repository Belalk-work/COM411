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

#multiple nested statement
print("where shall i look for the phone?")
place= input()
if place== "in the bedroom":
    print("where shall i look for in the bedroom?")
    bedroom_place= input()
    if bedroom_place== "under the bed":
        print("found girl's nickers, but no phone")
    else:
        print("i am so unlucky")
elif place== "in the bathroom":
        print("where shall i look for in the bathroom?")
bathroom_place= input()
if bathroom_place== "in the bathtub":
    print("fount rubber ducks but no phone")
else:
    print("found a ring")

elifplace= "in the living room"
print("where shall i look for in the living room?")
living_place= input()
if living_place== "on the table":
    print("yeees i found it")
else:
    print("just leave it")




