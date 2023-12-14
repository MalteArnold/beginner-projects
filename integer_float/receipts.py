# In this project, our goal is to create a receipt for the customers
# We need to define variables for the items, including descriptions and prices
# Then we need to calculate the total price with taxes and print the receipt

# 1. Step: define variables for the items
item1 = "Book"
item2 = "Computer"
item3 = "Monitor"
item4 = "Mouse"
item5 = "Keyboard"

# 2. Step: define variables for the description
item1_description = "A book about Python"
item2_description = "A computer for programming"
item3_description = "A monitor to see the code"
item4_description = "A mouse to navigate"
item5_description = "A keyboard to write code"

# 3. Step: define variables for the prices
item1_price = 20.99
item2_price = 999.99
item3_price = 199.99
item4_price = 29.99
item5_price = 99.99

# 4. Step: define variables for the taxes
tax_rate = 0.06

# Costumer one buys 2 books, 1 computer and 1 keyboard

# 5. Step: calculate the total price
subtotal = item1_price * 2 + item2_price + item5_price
tax = subtotal * tax_rate
total = subtotal + tax

# 6. Step: print the receipt
print("Your Receipt:")
print("2x " + item1 + ": " + item1_description + " - $" + str(item1_price * 2))
print(item2 + ": " + item2_description + " - $" + str(item2_price))
print(item5 + ": " + item5_description + " - $" + str(item5_price))
print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(tax))
print("Total: $" + str(total))

# 7. Step: round the tax and the total to two decimal places and print the receipt again
print("Your Receipt:")
print("2x " + item1 + ": " + item1_description + " - $" + str(item1_price * 2))
print(item2 + ": " + item2_description + " - $" + str(item2_price))
print(item5 + ": " + item5_description + " - $" + str(item5_price))
print("Subtotal: $" + str(subtotal))
print("Tax: $" + str(round(tax, 2)))
print("Total: $" + str(round(total, 2)))
