
animals = "monkey bat cat dog"

for a in animals.split(" "):
    print(a)

numbers = "65, 75, 32, 22"

list = []
count = 0
for n in numbers.split(", "):
    list.append(int(n))
print(f"{count}: {int(n)}")
count += 1

num_in_string = "zero, one, two, three, four, five"

list = []

for n in num_in_string.split(", "):
    if n == "zero":
        list.append(0)
    elif n == "one":
        list.append(1)
    elif n == "two":
        list.append(2)
    elif n == "three":
        list.append(3)
    elif n == "four":
        list.append(4)
    elif n == "five":
        list.append(5)

print(list)

win_lose_tie = "W W L T T W"

list = []

for c in win_lose_tie.split(" "):
    if c == "W":
        list.append(2)
    elif c == "T":
        list.append(1)
    elif c == "L":
        list.append(0)

print(list)

x_crd = "x:3, x:6, x:14, x:22"

list = []

for x in x_crd.split(", "):
    print(x[2:])
    list.append(int(x[2:]))

print(list)

x_y_crd = "x:2,y:5 - x:5,y:11 - x:7,y:14"
list = []

x_y = x_y_crd.split(" - ")

for xy in x_y:
    x_crd, y_crd = xy.split(",")

x = int(x_crd.split(":")[1])
y = int(y_crd.split(":")[1])

list.append([x,y])
print(list)