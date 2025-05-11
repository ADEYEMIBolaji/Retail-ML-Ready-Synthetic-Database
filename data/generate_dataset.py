# Re-import libraries and regenerate context after code execution state reset
import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Redefine sample data
payment_methods = ["Cash", "Mobile Money", "Card"]
card_types = ["Debit", "Credit"]
countries = ["UK", "US", "NG"]
payment_channels = ["Web", "POS", "Mobile App"]
locations = ["London", "Manchester", "Birmingham", "Leeds", "Glasgow"]
occupations = ["Engineer", "Doctor", "Teacher", "Analyst", "Trader"]

# Reconstruct product dictionary
expanded_products = {
    "Yam": "Tubers", "Cassava": "Tubers", "Sweet Potato": "Tubers",
    "Egusi": "Spices", "Suya Spice": "Spices", "Tumeric Powder": "Spices",
    "Plantain": "Fruits", "Orange": "Fruits", "Banana": "Fruits",
    "Jollof Rice Pack": "Grains", "Basmati Rice": "Grains",
    "Palm Oil": "Oil", "Groundnut Oil": "Oil",
    "Ogbono": "Seeds", "Beans": "Legumes",
    "Stockfish": "Proteins", "Dried Shrimps": "Proteins",
    "Chin Chin": "Snacks", "Plantain Chips": "Snacks", "Coconut Candy": "Snacks",
    "Toilet Roll": "Household", "Laundry Soap": "Household", "Dishwashing Liquid": "Household",
    "Indomie Noodles": "Convenience", "Sardines": "Convenience", "Spaghetti": "Convenience"
}

# Regenerate products
def generate_products(product_dict):
    prod_list = []
    for i, (name, cat) in enumerate(product_dict.items()):
        prod_list.append({
            "product_id": i,
            "product_name": name,
            "category": cat,
            "description": f"{name} - Premium quality",
            "price": round(np.random.uniform(1.5, 50.0), 2)
        })
    return pd.DataFrame(prod_list)

# Regenerate customers
def generate_customers(n_customers=1000):
    customers = []
    for i in range(n_customers):
        customers.append({
            "customer_id": i,
            "gender": random.choice(["Male", "Female"]),
            "age": random.randint(18, 65),
            "marital_status": random.choice(["Single", "Married"]),
            "occupation": random.choice(occupations),
            "location": random.choice(locations),
            "first_purchase_date": (datetime.now() - timedelta(days=random.randint(30, 730))).strftime("%Y-%m-%d"),
            "preferred_payment": random.choice(payment_methods),
        })
    return pd.DataFrame(customers)

# Generate consistent payments and purchases
def generate_consistent_payments_and_purchases(n=3000, customer_ids=None, product_df=None):
    payments = []
    purchases = []

    product_ids = product_df["product_id"].tolist()
    prod_price_map = product_df.set_index("product_id")["price"].to_dict()

    for i in range(n):
        product_id = random.choice(product_ids)
        unit_price = prod_price_map[product_id]
        quantity = random.randint(1, 5)
        total_amount = round(unit_price * quantity, 2)

        date_obj = datetime.now() - timedelta(days=random.randint(0, 60))
        transaction_date = date_obj.strftime("%Y-%m-%d")
        transaction_time = date_obj.strftime("%H:%M:%S")

        sales_channel = random.choice(["Online", "In-store"])
        valid_payment_methods = [pm for pm in payment_methods if not (sales_channel == "Online" and pm == "Cash")]
        payment_method = random.choice(valid_payment_methods)

        payment = {
            "payment_id": i,
            "payment_date": transaction_date,
            "payment_time": transaction_time,
            "amount": total_amount,
            "payment_method": payment_method,
            "card_type": random.choice(card_types),
            "issuer_country": random.choice(countries),
            "payment_channel": "Web" if sales_channel == "Online" else random.choice(["POS", "Mobile App"]),
            "avs_response": random.choice(["Y", "N", "U"]),
            "cvv_response": random.choice(["M", "N"]),
            "three_ds_response": random.choice(["Y", "N"]),
            "auth_response": random.choice(["Approved", "Declined"]),
            "merchant_name": f"Merchant_{random.randint(1, 50)}"
        }

        purchase = {
            "purchase_id": i,
            "customer_id": random.choice(customer_ids),
            "product_id": product_id,
            "purchase_date": transaction_date,
            "quantity": quantity,
            "total_amount": total_amount,
            "payment_id": i,
            "sales_channel": sales_channel
        }

        payments.append(payment)
        purchases.append(purchase)

    return pd.DataFrame(payments), pd.DataFrame(purchases)

# Generate data
products_df_full = generate_products(expanded_products)
customers_df_full = generate_customers()
payments_df_fixed, purchases_df_fixed = generate_consistent_payments_and_purchases(
    n=3000,
    customer_ids=customers_df_full["customer_id"].tolist(),
    product_df=products_df_full
)

# Save to CSV
products_df_full.to_csv("data/Products_Final.csv", index=False)
customers_df_full.to_csv("data/Customers_Final.csv", index=False)
payments_df_fixed.to_csv("data/Payments_Final.csv", index=False)
purchases_df_fixed.to_csv("data/Purchases_Final.csv", index=False)
