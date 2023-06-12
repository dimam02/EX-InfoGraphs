import matplotlib.pyplot as plt

countries = ['USA', 'Russia', 'China', 'India', 'ESA']
launch_counts = [415, 181, 145, 78, 84]

plt.bar(countries, launch_counts)
plt.xlabel('Country')
plt.ylabel('Number of Launches')
plt.title('Space Launches by Country')
plt.show()