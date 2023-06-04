import pandas as pd
import matplotlib.pyplot as plt

# Load the compressed CSV file from GitHub
url = 'https://github.com/ElshanKU/Airbnb./raw/main/calendar.csv.gz'
df = pd.read_csv(url, compression='gzip')

# Convert the 'date available' column to datetime format
df['date_available'] = pd.to_datetime(df['date available'])

# Extract month and year from the 'date available' column
df['month'] = df['date_available'].dt.month
df['year'] = df['date_available'].dt.year

# Group the data by month and calculate the average price
monthly_avg_prices = df.groupby(['year', 'month'])['price'].mean()

# Create a line plot to visualize the average prices over time
plt.figure(figsize=(10, 6))
monthly_avg_prices.plot()
plt.xlabel('Months')
plt.ylabel('Average Price')
plt.title('Average Prices of Listings Over Months')
plt.savefig('chart.png')
