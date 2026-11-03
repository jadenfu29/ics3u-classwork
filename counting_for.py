print("Type in a message, and I'll display it five times.")

message = input("Message: ")

# n can be short for number
#they control which numbers to loop between
# the third number controls how much to jump by
#calling it with only one number loops from 0 to that number, by 1 each time
#only using two numbers just loops between them by 1

for n in range(2, 21, 2):
    print(f"{n}. {message}")