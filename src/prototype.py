# Inventory Sales Tracker
# Emily Wishart
# Week 3
# This program stores inventory information for a small pottery business.

# Product 1 information
mug_name = "Mug"
mug_sku = "001"
mug_category = "Kitchenware"
mug_price = 8.50
mug_quantity = 100
mug_low_stock = 5
mug_active = True

# Product 2 information
bowl_name = "Bowl"
bowl_sku = "002"
bowl_category = "Kitchenware"
bowl_price = 6.50
bowl_quantity = 85
bowl_low_stock = 10
bowl_active = True

# Product 3 information
teapot_name = "Teapot"
teapot_sku = "003"
teapot_category = "Kitchenware"
teapot_price = 25.00
teapot_quantity = 30
teapot_low_stock = 5
teapot_active = True
#--------------------------------------------------------------------------------------

# Restock Inventory
print("Restock")
restock_amount = 10
print("Product:", teapot_name)
print("Starting Quantity:", teapot_quantity)

teapot_quantity = teapot_quantity + restock_amount
print("Restocked:", restock_amount)
print("New Quantity:", teapot_quantity)
#----------------------------------------------------------------------------------------------

# Record a sale
print("\nRecord Sale")
sale_amount = 3

print("Product:", mug_name)
print("Starting Quantity:", mug_quantity)

# Calculate the sale subtotal
subtotal = mug_price * sale_amount

# Subtract the sold items from inventory
mug_quantity = mug_quantity - sale_amount

print("Quantity Sold:", sale_amount)
print("Remaining Quantity:", mug_quantity)
#-------------------------------------------------------------------------------------------

# Inventory report
print("\nInventory Report")

print("Name:", mug_name, ", SKU:", mug_sku, ", Category:", mug_category,
f", Price: $ {mug_price:.2f}", ", Quantity:", mug_quantity)

print("Name:", bowl_name, ", SKU:", bowl_sku, ", Category:", bowl_category,
f", Price: $ {bowl_price:.2f}", ", Quantity:", bowl_quantity)

print("Name:", teapot_name, ", SKU:", teapot_sku, ", Category:", teapot_category,
f", Price: $ {teapot_price:.2f}", ", Quantity:", teapot_quantity)
#-------------------------------------------------------------------------------------------

# Sales receipt
print("\nSales Receipt")
print(mug_name, "x", sale_amount, "@ $" + format(mug_price, ".2f"), "=", "$" + format(subtotal, ".2f"))
