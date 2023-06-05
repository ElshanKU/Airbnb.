import pandas as pd
import matplotlib.pyplot as plt

# Load the compressed CSV file
df = pd.read_csv('calendar.csv.gz')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract month and year from 'date' column
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Group data by month and calculate average price
monthly_avg_prices = df.groupby(['year', 'month'])['price'].mean()

# Create a line plot to visualize the average prices over time
plt.figure(figsize=(10, 6))
monthly_avg_prices.plot()
plt.xlabel('Months')
plt.ylabel('Average Price')
plt.title('Average Prices of Listings Over Months')

# Save the chart as a PNG file
plt.savefig('chart.png')
