import random

#it always give the same thing with the same seed
random.seed(401)

x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()
print("Here are some random numbers from 1 to 5...")
# if we change the range from 1-5, the rng only picks between 1,2,3,4
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")