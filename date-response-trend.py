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

# Dates to highlight
highlight_ssv2024_dates = ['2023-09-06', '2023-09-13', '2023-09-20', '2023-09-22', '2023-09-28']
highlight_ssv2025_dates = ['2024-08-20', '2024-08-26', '2024-08-30', '2024-09-03']

# Convert highlight dates to 'Month-Day' format
highlight_ssv2024_dates = [pd.to_datetime(date).strftime('%m-%d') for date in highlight_ssv2024_dates]
highlight_ssv2025_dates = [pd.to_datetime(date).strftime('%m-%d') for date in highlight_ssv2025_dates]

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(volume_df.index, volume_df['SSV2024'], label='SSV2024', color='blue')
plt.plot(volume_df.index, volume_df['SSV2025'], label='SSV2025', color='red')

# Add vertical lines for highlighted dates with labels
for date in highlight_ssv2024_dates:
    plt.axvline(x=date, color='blue', linestyle='--', linewidth=1)
    plt.text(date, plt.ylim()[1], ' sent email', color='blue', rotation=90, verticalalignment='bottom')

for date in highlight_ssv2025_dates:
    plt.axvline(x=date, color='red', linestyle='--', linewidth=1)
    plt.text(date, plt.ylim()[1], ' sent email', color='red', rotation=90, verticalalignment='bottom')

plt.xlabel('Date (Month-Day)')
plt.ylabel('Volume')
plt.legend(title='Project Year')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('volume_over_time.png')

# Show the plot
plt.show()
