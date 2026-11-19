import random
nums = [random.randrange(100) for i in range(10)]
x = int(input("What number: "))
counter = 0
for number in nums:
    if x ==number:
        counter+=1
print(f"found {coounter} times")