import random
nums = [random.randrange(100) for i in range(10)]
x = int(input("What number: "))
for number in nums:
    if x ==number:
        print(f"found")
        break
else:
    print("Not found")
