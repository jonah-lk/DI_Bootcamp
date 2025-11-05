# In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior.
# The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

product_total_sales = {}
customer_total_purchases = {}
high_value_transactions = []
purchase_by_customer = {}
most_popular_product = {}
for sale in sales_data:
    # Total Sales Calculation: Calculate the total sales for each product category
    # (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.
    try:
        product_total_sales[sale['product']]['revenue'] += sale['price'] * sale['quantity']
    except:
        product_total_sales[sale['product']] = {
            'revenue': sale['price'] * sale['quantity']
        }
    # Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.
    try:
        customer_total_purchases[sale['customer_id']] += sale['price'] * sale['quantity']
    except:
        customer_total_purchases[sale['customer_id']] = sale['price'] * sale['quantity']
    # Sales Data Enhancement:
    # Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
    # Use a loop to modify the sales_data list with this new information.
    sale['total_price'] = sale['price'] * sale['quantity']
    # High-Value Transactions:
    # Using list comprehension, create a list of all transactions where the total price is greater than $500.
    # Sort this list by the total price in descending order.
    if sale['total_price'] > 500:
        high_value_transactions.append(sale['total_price'])
    # Customer Loyalty Identification:
    # Identify any customer who has made more than one purchase, suggesting potential loyalty.
    # Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.
    try:
        purchase_by_customer[sale['customer_id']]['purchases'] += 1
        purchase_by_customer[sale['customer_id']]['loyal'] = True
    except:
        purchase_by_customer[sale['customer_id']] = {
            'purchases': 1,
            'loyal': False
        }
    # Bonus: Insights and Analysis:
    # Calculate the average transaction value for each product category.
    try:
        product_total_sales[sale['product']]['quantity_sold'] += sale['quantity']
        product_total_sales[sale['product']]['average_value'] = round(product_total_sales[sale['product']]['revenue'] / product_total_sales[sale['product']]['quantity_sold'], 2)
    except:
        product_total_sales[sale['product']]['quantity_sold'] = sale['quantity']
        product_total_sales[sale['product']]['average_value'] = round(product_total_sales[sale['product']]['revenue'] / sale['quantity'], 2)
    # Identify the most popular product based on the quantity sold.
    try:
        if sale['product'] != most_popular_product[sale['product']] and most_popular_product[sale['product']] > sale['quantity']:
            most_popular_product.clear()
            most_popular_product[sale['product']] = product_total_sales[sale['product']]['quantity_sold']
    except:
        most_popular_product[sale['product']] = product_total_sales[sale['product']]['quantity_sold']
high_value_transactions.sort(reverse = True)
# Provide insights into how these analyses could inform the company’s marketing strategies.
# Valid information to recognize the best sellers and worst selling products.
# That information can help the company better plan their restocking orders and also possible cancellation/unshelving of bad performing products.
# For advertisng purposes, we basically highlight what to focus the advertising budget on.
# By that I mean the best performing may need cuts to their budgets since word is already out;
# or the budget is insufficient for bad perfoming but promissing products etc...