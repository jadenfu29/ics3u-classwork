import random
guess1=0
guess2=1
while guess1!=guess2:
    guess1 = random.randrange(1,7)
    guess2 = random.randrange(1,7)
    print(f"{guess1} {guess2}")