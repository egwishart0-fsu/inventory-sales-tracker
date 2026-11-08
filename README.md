Inventory-sales-tracker
---------------------------------------------------------------------------------------------------------------------------
Emily Wishart
Semester Project: Small Store

Week 2
---------------------------------------------------------------------------------------------------------------------------
Progress: Created an initial prototype, with a price, and subtotal calculation.

Week 3
---------------------------------------------------------------------------------------------------------------------------
Progress: Added 2 more products, along with product detail information, stock, and sales.

-----Product detail Information-----
SKU: product unique identification number
Name: name of product
Category: type of product
Unit Price: price of one product
Quantity: current quantity in stock
Low-Stock Threshold: minimum quantity in stock before considered "low in stock"
Active Status: whether product is being sold or not

-----State Trace for restock and sale-----
Product: Teapot
Starting Quantity: 30
Restocked: 10
New Quantity: 40

Record Sale
Product: Mug
Starting Quantity: 100
Quantity Sold: 3
Remaining Quantity: 97

-----Expected Output below after restock and sale, matched the actual output-----
Inventory Report
Name: Mug , SKU: 001 , Category: Kitchenware , Price: $ 8.50 , Quantity: 97
Name: Bowl , SKU: 002 , Category: Kitchenware , Price: $ 6.50 , Quantity: 85
Name: Teapot , SKU: 003 , Category: Kitchenware , Price: $ 25.00 , Quantity: 40

Sales Receipt
Mug x 3 @ $8.50 = $25.50

Week 4
---------------------------------------------------------------------------------------------------------------------------
Progress: Created validation check for nonempty SKU/name/category, positive price, nonnegative inventory, and positive sales 
quantity. Also added a check for existing duplicates for a new SKU. Rejected sales higher than the available quantity which cancels sale.

Test 1: Duplicate SKU, valid sale, and blank name. Expect an error message for duplicate SKU and blank name. Expect sale to run and report subtotal. Actual results matched expected results.

#only pasted meaningful outputs

Product Validation
Mug: Product Information is Valid
Bowl: Product Information is Valid
Teapot: Invalid: Name cannot be blank
New SKU rejected: duplicate SKU already exists

Record Sale
Product: Mug
Starting Quantity: 100
Quantity Sold: 3
Remaining Quantity: 97

Sales Receipt
Mug x 3 @ $8.50 = $25.50

Test 2: Oversell attempt, expect sale to be rejected. Actual results matched expected results.

#meaningful outputs

Record Sale
Sale Rejected: Invalid Sale Amount



