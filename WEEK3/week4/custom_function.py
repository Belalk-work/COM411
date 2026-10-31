#parameter
def escape_by(plan):
    if plan == "jump over":
#displayed messages
        print("we cant escape that way, because the boulder is too big")
    elif plan == "running around":
        print("we cant escape that way, because the boulder is too fast")
    elif plan == "cross the bridge ahead":
        print("that might just work,lets go")
    else:
        print("we cannot escape that way , beacuse the boulder is on the way")
#call to function
escape_by("jump over")
escape_by("running around")
escape_by("cross the bridge ahead")
escape_by("")






