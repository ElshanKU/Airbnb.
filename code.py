import pandas as pd
import matplotlib.pyplot as plt

# Load the compressed CSV file
df = pd.read_csv('calendar.csv.gz')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract month from 'date' column
df['month'] = df['date'].dt.strftime('%B')

# Convert 'price' column to numeric values, ignore any non-numeric values
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Remove rows with NaN (non-numeric) values in the 'price' column
df = df.dropna(subset=['price'])

# Define custom order for months
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

# Group data by month and calculate average price
monthly_avg_prices = df.groupby('month')['price'].mean()

# Create a line plot to visualize the average prices over time
plt.figure(figsize=(10, 6))
monthly_avg_prices.loc[month_order].plot(marker='o')
plt.xlabel('Months')
plt.ylabel('Price ($)')
plt.title('Average Prices of Listings Over Months')

# Customize the y-axis tick labels
plt.yticks([50, 150, 350, 500, 1000])

# Save the chart as a PNG file
plt.savefig('chart.png')

