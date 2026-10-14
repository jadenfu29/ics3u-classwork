tries = 0
guess = int(input("Guess my number 1-18: "))
if guess!=7:
    tries+=1
    guess=int(input("Guess my number 1-18: "))
print(tries)