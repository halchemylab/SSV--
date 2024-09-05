import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('SSV_Combined_Data.csv')

# Convert the 'Start Date' column to datetime format
df['Start Date'] = pd.to_datetime(df['Start Date'])

# Extract the month and day from the 'Start Date' column
df['Month-Day'] = df['Start Date'].dt.strftime('%m-%d')

# Group by 'Month-Day' and 'Project' and count the occurrences
volume_df = df.groupby(['Month-Day', 'Project']).size().unstack(fill_value=0)

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(volume_df.index, volume_df['SSV2024'], label='SSV2024', color='blue')
plt.plot(volume_df.index, volume_df['SSV2025'], label='SSV2025', color='red')
plt.xlabel('Date (Month-Day)')
plt.ylabel('Volume')
plt.title('Volume over Time for Projects SSV2024 and SSV2025')
plt.legend(title='Project')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('volume_over_time.png')

# Show the plot
plt.show()
