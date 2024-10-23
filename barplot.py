import matplotlib.pyplot as plt

# Plotting the count of Gender
dataset['Gender'].value_counts().plot(kind='bar', color='red')
plt.title('Count of People by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


import matplotlib.pyplot as plt

# Grouping by Gender and plotting the average Age
dataset.groupby('Gender')['Age'].mean().plot(kind='bar', color='red')
plt.title('Average Age by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Age')
plt.show()