import pandas as pd
import matplotlib.pyplot as plt

# Load the compressed CSV file
df = pd.read_csv('calendar.csv.gz')

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract month and year from 'date' column
df['month'] = df['date'].dt.strftime('%B')
df['year'] = df['date'].dt.year

# Convert 'price' column to numeric values, ignore any non-numeric values
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Filter data for January and February of 2024
filtered_df = df[(df['month'].isin(['January', 'February'])) & (df['year'] == 2024)]

# Create a line plot using filtered data
plt.figure(figsize=(10, 6))
plt.plot(filtered_df['date'], filtered_df['price'], marker='o')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.title('Price of Listings in January and February 2024')

# Customize the y-axis tick labels
plt.yticks([150, 200, 350])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Save the chart as a PNG file
plt.savefig('chart.png')
