import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/Sample - Superstore.csv")

# 1. Most profitable categories
profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print(profit_by_category)

# 2. Visualization
profit_by_category.plot(kind='bar', title='Profit by Category')
plt.savefig('images/profit_by_category.png')
plt.show()