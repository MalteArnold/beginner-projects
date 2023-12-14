# In this project, our aim is to create a shopping list
# We want to calculate the total price of the items

# 1. Step: define price for the items
item1 = 20.99
item2 = 999.99
item3 = 199.99
item4 = 29.99
item5 = 99.99

# 2. Step: define the quantity of the items
item1_quantity = 2
item2_quantity = 0
item3_quantity = 1
item4_quantity = 4
item5_quantity = 7

# 3. Step: calculate the total price per item
item1_total = item1 * item1_quantity
item2_total = item2 * item2_quantity
item3_total = item3 * item3_quantity
item4_total = item4 * item4_quantity
item5_total = item5 * item5_quantity

# 4. Step: calculate the total price of all items and print it
total = item1_total + item2_total + item3_total + item4_total + item5_total
print("Total: $" + str(total))
