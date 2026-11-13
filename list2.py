import random
nums = []
for i in range(10):
    nums.append(random.randrange(1,101))
for i in range(len(nums)):
    print(nums[i])