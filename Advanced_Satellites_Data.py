import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a CSV file named 'UCS-Satellite-Database-5-1-2022 - Sheet1.csv' with columns 'Year' and 'Type'
# Load the dataset
df = pd.read_csv('/Users/Dmytro/Downloads/UCS-Satellite-Database-5-1-2022 - Sheet1.csv')


# Group the data by year and count the number of satellites of each type
satellite_counts = df.groupby(['Year', 'Type']).size().unstack(fill_value=0)

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))
satellite_counts.plot(kind='bar', stacked=True, ax=ax)

# Set labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Satellites')
ax.set_title('Types of Satellites Launched Each Year')

# Show the legend
ax.legend(title='Satellite Type')

# Show the plot
plt.show()