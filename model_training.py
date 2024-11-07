import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the fully cleaned data
df = pd.read_csv('georgia_census_data_fully_cleaned.csv')

# Initialize a dictionary to store MSE results for each city
results = {}

# Iterate over each unique city
for city in df['Place Name'].unique():
    print(f"\nTraining model for {city}...")
    
    # Filter the dataset for the current city
    city_data = df[df['Place Name'] == city]
    
    # Check if growth rate columns exist; if not, create them with default values
    if 'Rent Growth Rate' not in city_data.columns:
        city_data = city_data.copy()
        city_data['Rent Growth Rate'] = 0
    if 'Income Growth Rate' not in city_data.columns:
        city_data = city_data.copy()
        city_data['Income Growth Rate'] = 0

    # Define features and target
    features = city_data[['Median Household Income', 'Total Population', 'Labor Force Participation', 
                          'Rent Growth Rate', 'Income Growth Rate']]
    target = city_data['Median Home Value']
    
    # Handle any remaining NaNs by filling with the median
    features = features.fillna(features.median())
    
    # Check if we have enough data to perform a split
    if len(features) < 2:
        print(f"Not enough data to train/test split for {city}. Skipping this city.")
        continue

    # Split city-specific data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Standardize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Initialize and train the model (Random Forest as an example)
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Predict on the test set and calculate MSE
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    results[city] = mse  # Store the MSE for this city
    print(f"{city} - Mean Squared Error: {mse}")

# Display MSE results for each city
print("\nMSE for each city:\n", results)

# Optionally, save results to a CSV for record-keeping
results_df = pd.DataFrame(list(results.items()), columns=['City', 'MSE'])
results_df.to_csv('city_mse_results.csv', index=False)
print("MSE results saved to 'city_mse_results.csv'")