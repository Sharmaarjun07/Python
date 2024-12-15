import pandas as pd

# Given age data
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# Define bins and labels
bins = [0, 25, 35, 60, float('inf')]
labels = ['Youth', 'Young Adult', 'Middle Aged', 'Senior']

# Create a DataFrame and assign categories
df = pd.DataFrame({'Age': ages})
df['Category'] = pd.cut(df['Age'], bins=bins, labels=labels)

print(df)




print("_________________________________________")
import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [32, 75, 30, 72],
}

df = pd.DataFrame(data)

# Pivoting the data
pivoted_df = df.pivot(index='Date', columns='City', values='Temperature')
print(pivoted_df)
print("___________________")
# Continuing from the pivoted_df example

# Stacking the data
stacked_df = pivoted_df.stack()
print(stacked_df)
