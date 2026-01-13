name=int(input("enter the name"))
print(name)
age=int(input("enter an age"))
print(age)
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product': ['A', 'B', 'C', 'D'],
    'Sales': [1200, 1800, 1000, 1500]
}

df = pd.DataFrame(data)
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)
top_product = df.loc[df['Sales'].idxmax()]
print("Top Selling Product:", top_product['Product'])
print("Sales Amount:", top_product['Sales'])
plt.bar(df['Product'], df['Sales'])
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales Analysis")
plt.show 