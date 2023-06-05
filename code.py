import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import gzip

# Load the compressed CSV file
with gzip.open('calendar.csv.gz', 'rt') as file:
    df = pd.read_csv(file)

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Filter data for January and February of 2024
filtered_df = df[(df['date'].dt.month.isin([1, 2])) & (df['date'].dt.year == 2024)]

# Extract month from 'date' column
filtered_df['month'] = filtered_df['date'].dt.strftime('%B')

# Convert 'price' column to numeric values, ignore any non-numeric values
filtered_df['price'] = pd.to_numeric(filtered_df['price'], errors='coerce')

# Define the custom order for months
month_order = ['January', 'February']

# Create a bar plot using seaborn
plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_df, x='month', y='price', order=month_order, color='skyblue')
plt.xlabel('Months')
plt.ylabel('Price ($)')
plt.title('Average Prices of Listings in January and February 2024')

# Customize the y-axis tick labels
plt.yticks([150, 350, 500, 750, 1000])

# Save the chart as a PNG file
plt.savefig('chart.png')
