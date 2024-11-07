# feature_engineering_and_split.py

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the fully cleaned data
df = pd.read_csv('georgia_census_data_fully_cleaned.csv')

# Feature Engineering: Calculate year-over-year growth rates for key variables
df['Home Value Growth Rate'] = df.groupby('Place Name')['Median Home Value'].pct_change()
df['Rent Growth Rate'] = df.groupby('Place Name')['Median Rent'].pct_change()
df['Income Growth Rate'] = df.groupby('Place Name')['Median Household Income'].pct_change()

# Select features and target for modeling
features = df[['Median Household Income', 'Total Population', 'Labor Force Participation', 
               'Rent Growth Rate', 'Income Growth Rate']]
target = df['Median Home Value']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Save the train-test split data for use in model training
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)
print("Feature engineering and train-test split completed. Data saved for model training.")