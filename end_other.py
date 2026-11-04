a = list(input())
b = list(input())
a.reverse()
b.reverse()
for i in range(len(b)):
    if a[i].lower()!=b[i].lower():
        print(False)
        break
else:
    print(True)