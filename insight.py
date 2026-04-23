import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('Campaign_Data_Week1')

# Filter for New Customers
new_customers = df[df['Customer Type'] == 'New']

# Aggregate Sales for Chart 1
sales_agg = new_customers.groupby(['Campaign Type', 'Channel'])['Sales ($)'].sum().reset_index()
sales_agg = sales_agg.sort_values('Sales ($)', ascending=False)

# Aggregate Conversion Rate for Chart 2
conv_agg = new_customers.groupby(['Campaign Type', 'Channel'])['Converted (1=yes, 0=no)'].mean().reset_index()
conv_agg['Conversion Rate (%)'] = conv_agg['Converted (1=yes, 0=no)'] * 100
conv_agg = conv_agg.sort_values('Conversion Rate (%)', ascending=False)

# Set style
sns.set_theme(style="whitegrid")

# Create Chart 1: Total Sales by Combo (New Customers)
plt.figure(figsize=(10, 6))
sns.barplot(data=sales_agg, x='Channel', y='Sales ($)', hue='Campaign Type')
plt.title('Total Sales by Campaign & Channel (New Customers Only)')
plt.ylabel('Total Sales ($)')
plt.xlabel('Marketing Channel')
plt.legend(title='Campaign Type')
plt.tight_layout()
plt.savefig('new_customer_sales_by_combo.png')
plt.close()

# Create Chart 2: Conversion Rate by Combo (New Customers)
plt.figure(figsize=(10, 6))
sns.barplot(data=conv_agg, x='Channel', y='Conversion Rate (%)', hue='Campaign Type')
plt.title('Conversion Rate by Campaign & Channel (New Customers Only)')
plt.ylabel('Conversion Rate (%)')
plt.xlabel('Marketing Channel')
plt.legend(title='Campaign Type')
plt.tight_layout()
plt.savefig('new_customer_conv_rate.png')
plt.close()

print(sales_agg)
print(conv_agg)
