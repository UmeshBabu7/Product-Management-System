import pandas as pd

# Sample product data
data = [
    {"sku": "SKU0001", "name": "Product 1", "category": "Clothing", "price": 232.54, "stock_qty": 189, "status": "inactive"},
    {"sku": "SKU0002", "name": "Product 2", "category": "Electronics", "price": 337.42, "stock_qty": 60, "status": "active"},
    {"sku": "SKU0003", "name": "Product 3", "category": "Home", "price": 416.91, "stock_qty": 104, "status": "inactive"},
    {"sku": "SKU0004", "name": "Product 4", "category": "Clothing", "price": 168.42, "stock_qty": 120, "status": "inactive"},
    {"sku": "SKU0005", "name": "Product 5", "category": "Sports", "price": 129.23, "stock_qty": 75, "status": "active"},
    {"sku": "SKU0006", "name": "Product 6", "category": "Books", "price": 92.22, "stock_qty": 136, "status": "active"},
    {"sku": "SKU0007", "name": "Product 7", "category": "Beauty", "price": 100.22, "stock_qty": 60, "status": "active"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv('sample_products.csv', index=False)
print("Sample CSV file created: sample_products.csv")

# Save as Excel
df.to_excel('sample_products.xlsx', index=False)
print("Sample Excel file created: sample_products.xlsx")

print(f"Created sample files with {len(data)} products")
