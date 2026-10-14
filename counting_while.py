print("Type in a message, and I'll display it five times.")

message = input("Message: ")
print()

n = 0
while n < 100:
    print(f"{n + 1}. {message}")
    # increments n by 1 each time
    n += 10