tries = 0
guess = int(input("Guess my number 1-18: "))
while guess!=32 and tries<9:
    print(tries)
    guess=int(input("Guess my number 1-18: "))
print(tries)