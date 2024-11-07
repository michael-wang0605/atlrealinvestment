import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
df = pd.read_csv('georgia_census_data_all_years.csv')

# Replace all instances of -666666666 with NaN
df.replace(-666666666, np.nan, inplace=True)

# Save the cleaned data (optional intermediate save)
df.to_csv('georgia_census_data_cleaned.csv', index=False)
print("Data cleaned and saved to 'georgia_census_data_cleaned.csv'")

# Replace missing values by assigning the result back to the column
df['Median Home Value'] = df['Median Home Value'].fillna(df['Median Home Value'].median())
df['Median Rent'] = df['Median Rent'].fillna(df['Median Rent'].median())
df['Median Household Income'] = df['Median Household Income'].fillna(df['Median Household Income'].median())

# Save the fully cleaned data
df.to_csv('georgia_census_data_fully_cleaned.csv', index=False)
print("Fully cleaned data saved to 'georgia_census_data_fully_cleaned.csv'")

# Display the count of missing values per column
missing_data = df.isnull().sum()
print("Missing values per column:\n", missing_data)

# Step 1: Descriptive Statistics
print("\nSummary Statistics:")
print(df.describe())

# Step 2: Visualize Distributions
plt.figure(figsize=(12, 8))
df[['Median Home Value', 'Median Rent', 'Median Household Income']].hist(bins=30, figsize=(12, 8))
plt.suptitle("Distribution of Key Variables", fontsize=16)
plt.show()

# Step 3: Analyze Trends Over Time
plt.figure(figsize=(10, 6))
df.groupby('Year')[['Median Home Value', 'Median Rent', 'Median Household Income']].mean().plot()
plt.title("Trends Over Time")
plt.ylabel("Values")
plt.show()

# Step 4: Explore Relationships Between Variables
plt.figure(figsize=(8, 6))
plt.scatter(df['Median Household Income'], df['Median Home Value'], alpha=0.5)
plt.title("Median Household Income vs. Median Home Value")
plt.xlabel("Median Household Income")
plt.ylabel("Median Home Value")
plt.show()

# Step 5: Correlation Analysis
corr_matrix = df.corr()
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()