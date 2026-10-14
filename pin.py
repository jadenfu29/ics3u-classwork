PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

#while loops are just if statements that repeat until false
#we would have to take in int(input())
while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    #commenting it out makes it an infinte loop because the entry never changes


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")