
while True:
    side1 = int(input())
    if num>0:
        break
    else:
        print("Retry")
while True:
    side2 = int(input())
    if num>0 and side2>=side1:
        break
    else:
        print("Retry")
while True:
    side3 = int(input())
    if num>0 and side3>=side2:
        break
    else:
        print("Retry")
if side1*side1+side2*side2 == side3*side3:
    print("It is a right triangle")
else:
    print("Its not a right triangle")