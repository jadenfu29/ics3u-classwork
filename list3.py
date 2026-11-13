import random
nums = []
for i in range(1000):
    nums.append(random.randrange(10,100))
for i in range(len(nums)):
    print(nums[i])