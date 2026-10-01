age = int(input())
if age<16:
    print("You cannot drive")
elif 16<=age<=17:
    print("You can drive but not vote")
elif 18<=age<=20:
    print("You can vote but not drive a car")
else:
    print("You can do pretty much anything")