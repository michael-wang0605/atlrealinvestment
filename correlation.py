import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy.stats import ttest_ind

# Load the fully cleaned data
df = pd.read_csv('georgia_census_data_fully_cleaned.csv')

# Compute Price-to-Rent Ratio
df['Price-to-Rent Ratio'] = df['Median Home Value'] / df['Median Rent']

# Filter data to exclude rows with missing Price-to-Rent Ratio
df = df.dropna(subset=['Price-to-Rent Ratio'])

### 1. Correlation Analysis
# Filter to include only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# Compute and plot the correlation matrix
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numeric Features')
plt.show()

### 2. Feature Importance via Linear Regression
# Define features and target for regression
features = df[['Median Household Income', 'Total Population', 'Labor Force Participation',
               'Educational Attainment (Total)', 'Total Housing Units', 'Occupied Units',
               'Vacant Units', 'Owner-Occupied Units']]
target = df['Price-to-Rent Ratio']

# Fit linear regression model
lin_reg = LinearRegression()
lin_reg.fit(features, target)

# Display feature importance
feature_importance = pd.Series(lin_reg.coef_, index=features.columns)
feature_importance = feature_importance.abs().sort_values(ascending=False)  # Sort by absolute importance
print("Feature Importance (Linear Regression Coefficients):")
print(feature_importance)

# Plot feature importance
feature_importance.plot(kind='bar')
plt.title('Feature Importance for Price-to-Rent Ratio')
plt.show()

### 3. Statistical Test (Example using cities with high vs. low MSE)
# Assume 'results' dictionary contains MSE values for each city
# Separate high-error and low-error cities for comparison
threshold = 1.0  # Set a threshold for separating high and low MSE, adjust based on your data
high_mse_cities = df[df['Place Name'].isin([city for city, mse in results.items() if mse > threshold])]
low_mse_cities = df[df['Place Name'].isin([city for city, mse in results.items() if mse <= threshold])]

# T-test for Median Household Income as an example
ttest_income = ttest_ind(high_mse_cities['Median Household Income'], low_mse_cities['Median Household Income'], nan_policy='omit')
print(f"T-test result for Median Household Income between high and low MSE cities: {ttest_income}")

# Adjust the size of the heatmap and rotate labels for better readability
plt.figure(figsize=(12, 10))  # Set the figure size

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", 
            annot_kws={"size": 8})  # Reduce annotation size if needed
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.yticks(rotation=0)  # Keep y-axis labels horizontal
plt.title('Correlation Matrix of Numeric Features')
plt.tight_layout()  # Adjust layout to fit labels
plt.show()