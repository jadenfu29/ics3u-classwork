import random
print("Guess a number 1-10")
guess = int(input("Guess: "))
x = random.randrange(1,11)
if guess==x:
    print("You guessed correct")
else:
    print(f"The number was {x}")