import pandas as pd
import matplotlib.pyplot as plt
import gzip

# Load the compressed CSV file
with gzip.open('calendar.csv.gz', 'rt') as file:
    df = pd.read_csv(file)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for January and February of 2024
filtered_df = df[(df['date'].dt.month.isin([1, 2])) & (df['date'].dt.year == 2024)]

# Extract month and year from 'date' column
filtered_df['month'] = filtered_df['date'].dt.strftime('%B')

# Convert 'price' column to numeric values, ignore any non-numeric values
filtered_df['price'] = pd.to_numeric(filtered_df['price'], errors='coerce')

# Group data by month and calculate average price
monthly_avg_prices = filtered_df.groupby('month')['price'].mean()

# Define the custom order for months
month_order = ['January', 'February']

# Create a column chart using the average prices
plt.figure(figsize=(10, 6))
plt.bar(monthly_avg_prices.index, monthly_avg_prices.values, color='skyblue')
plt.xlabel('Months')
plt.ylabel('Price ($)')
plt.title('Average Prices of Listings in January and February 2024')

# Customize the y-axis tick labels
plt.yticks([150, 350, 500, 750, 1000])

# Save the chart as a PNG file
plt.savefig('chart.png')
