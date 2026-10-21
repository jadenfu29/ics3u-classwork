import random

while True:
    guess1 = random.randrange(1,7)
    guess2 = random.randrange(1,7)
    print(f"{guess1} {guess2}")
    if guess1==guess2:
        break