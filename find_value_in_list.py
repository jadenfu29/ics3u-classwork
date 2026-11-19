import random
nums = [random.randrange(100) for i in range(10)]
x = int(input("What number: "))
for number in nums:
    if x ==number:
        print(f"{number} is in the list")