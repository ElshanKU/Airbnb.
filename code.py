import pandas as pd
import matplotlib.pyplot as plt

# Load the compressed CSV file from GitHub
url = 'https://github.com/ElshanKU/Airbnb./raw/main/calendar.csv.gz'
df = pd.read_csv(url, compression='gzip')

# Convert the 'date available' column to datetime format
df['date_available'] = pd.to_datetime(df['date available'])

# Extract month from the 'date available' column
df['month'] = df['date_available'].dt.month

# Group the data by month and calculate the average price
monthly_avg_prices = df.groupby('month')['price'].mean()

# Create a bar plot to visualize the average prices by month
plt.bar(monthly_avg_prices.index, monthly_avg_prices.values)
plt.xlabel('Month')
plt.ylabel('Average Price')
plt.title('Average Prices of Listings by Month')
plt.show()
