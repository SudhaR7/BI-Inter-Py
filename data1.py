import pandas as pd
# Creating an extended DataFrame
df = pd.DataFrame({
    'Fname': ['Alex', 'Harry', 'Maria', 'John', 'Sophia', 'Ella'],
    'Lname': ['Smith', 'Potter', 'Gonzalez', 'Doe', 'Brown', 'Johnson'],
    'Age': [20, 21, 22, 23, 21, 24],
    'Gender': ['M', 'M', 'F', 'M', 'F', 'F'],
    'Country': ['USA', 'UK', 'Spain', 'USA', 'Canada', 'Australia']
})

# Display the DataFrame
print("Initial DataFrame:")
print(df)

# Descriptive statistics of numerical data
print("\nDescriptive statistics:")
print(df.describe())