import random
nums = [random.randrange(100) for i in range(10)]
x = int(input("What number: "))
for i in range(len(nums)):
    if x ==nums[number]:
        print(f"found at {i}")
        break
else:
    print("Not found")
