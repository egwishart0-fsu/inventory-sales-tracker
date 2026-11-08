# Inventory Sales Tracker
# Emily Wishart
# Week 4
# This program validates information, stores inventory, and runs sales for a small pottery business.

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
# Validate Product Information
print("\nProduct Validation")
def validate_product(name, sku, category, price, quantity):
    if name.strip() == "":
        raise ValueError ("Name cannot be blank")
    if sku.strip() == "":
        raise ValueError ("SKU cannot be blank")
    if category.strip() == "":
        raise ValueError ("Category cannot be blank")
    if price <= 0:
        raise ValueError ("Price must be greater than 0")
    if quantity < 0:
        raise ValueError ("Quantity must be greater than or equal to 0")


try:
    validate_product(mug_name, mug_sku, mug_category, mug_price, mug_quantity)
    print("Mug: Product Information is Valid")
except ValueError as error:
    print("Mug: Invalid:", error)

try:
    validate_product(bowl_name, bowl_sku, bowl_category, bowl_price, bowl_quantity)
    print("Bowl: Product Information is Valid")
except ValueError as error:
    print("Bowl: Invalid:", error)

try:
    validate_product(teapot_name, teapot_sku, teapot_category, teapot_price, teapot_quantity)
    print("Teapot: Product Information is Valid")
except ValueError as error:
    print("Teapot: Invalid:", error)

# Check for Duplicate SKU
def validate_sku(new_sku, existing_skus):
    for sku in existing_skus:
        if new_sku == sku:
            raise ValueError("SKU already exists")
    print("SKU is available")

# Test Duplicate SKU
existing_skus = [mug_sku, bowl_sku, teapot_sku]
try:
    validate_sku("001", existing_skus)

except ValueError as error:
    print("New SKU rejected: duplicate", error)

#-------------------------------------------------------------------------------------------------------

# Restock Inventory
print("\nRestock")
restock_amount = 10
print("Product:", teapot_name)
print("Starting Quantity:", teapot_quantity)

teapot_quantity = teapot_quantity + restock_amount
print("Restocked:", restock_amount)
print("New Quantity:", teapot_quantity)
#----------------------------------------------------------------------------------------------

# Record a Sale
print("\nRecord Sale")
sale_amount = 3

def validate_sale_amount(sale_amount):
    if sale_amount <= 0 or sale_amount > mug_quantity::
        raise ValueError("Invalid Sale Amount")
    return sale_amount

try:
    validate_sale_amount(sale_amount)

    print("Product:", mug_name)
    print("Starting Quantity:", mug_quantity)

    # Calculate the sale subtotal
    subtotal = mug_price * sale_amount

    # Subtract sold items from inventory
    mug_quantity = mug_quantity - sale_amount

    print("Quantity Sold:", sale_amount)
    print("Remaining Quantity:", mug_quantity)

    # Sales receipt
    print("\nSales Receipt")
    print(mug_name, "x", sale_amount, "@ $" + format(mug_price, ".2f"), "=", "$" + format(subtotal, ".2f"))

except ValueError as error:
    print("Sale Rejected:", error)
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

