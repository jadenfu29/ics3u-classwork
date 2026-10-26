counter = 0
while True:
    guess = int(input("Guess: "))
    counter+=1
    if guess == 6:
        break
print("Good")
print(counter)