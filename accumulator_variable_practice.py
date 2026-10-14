n = 1
counter = 0
while n<=10:
    counter+=n
    n+=1
print(counter)

n=100
counter=0
while n<=200:
    counter+=n
    n+=1
print(counter)

print(-101*100)
#this will always be the same no matter if its 200-300, or 400-500...

n=1000
counter=0

while n<=10000:
    counter+=n
    n+=5
print(counter)

n=5
counter = 0
while n<=100:
    if n%3!=0:
        counter+=n
    n+=5
print(counter)