print("Enter the following information about an item you wish to purchase..")
print()


name = input("The name of the item:")
#the price is taken as a float while the name is taken as a string
price = float(input("The price: $"))

#switching the order would make the code take the input first, then output the prompt which doesnt make sense
quantity = int(input("How many do you want?"))
# by removing the int, the code would think that the quantity is a string by default and you would not be able to multiply the tax to it
subtotal = price * quantity
tax = subtotal * 0.13
total = subtotal + tax

print()
print(f"You choose to buy {quantity} {name}.")
print(f"That will come out to ${total}")
