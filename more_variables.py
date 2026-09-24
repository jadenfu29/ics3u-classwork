store = "No Frills"
item = "Apples"
price = 0.6
quantity = 7000000
subtotal = price * quantity
tax = subtotal * 0.05
total = tax + subtotal
#f string
print(f"At {store} I bought some {item}.")
#concatenation
print("They sold for $" + str(price) + " each.")
#dot format
print("I wanted to purchase {} of them.".format(quantity))
#f string
print(f"The total price, with tax included, was ${total}.")
print(f"The subtotal and tax amounts are ${subtotal} and ${tax}")