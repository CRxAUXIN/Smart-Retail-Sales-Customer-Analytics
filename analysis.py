
import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv('sales.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
inventory = pd.read_csv('inventory.csv')

sales['Total_Sales'] = sales['Quantity'] * sales['Price']

monthly = sales.groupby(sales['Date'].astype('datetime64[M]'))['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
