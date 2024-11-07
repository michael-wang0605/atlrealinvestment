import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from itertools import product

# Load the fully cleaned data
df = pd.read_csv('georgia_census_data_fully_cleaned.csv')

# Initialize a dictionary to store MSE results for each city
results = {}

# Define parameter ranges for p, d, and q
p_values = [0, 1, 2]
d_values = [0, 1]
q_values = [0, 1, 2]
param_grid = list(product(p_values, d_values, q_values))

# Create a folder for all visualizations
visualization_folder = "results"
os.makedirs(visualization_folder, exist_ok=True)  # Create the directory if it doesn't exist

# Iterate over each unique city
for city_name in df['Place Name'].unique():
    city_data = df[df['Place Name'] == city_name].sort_values(by='Year')

    # Ensure there are enough data points for the ARIMA model
    if len(city_data) < 3:
        print(f"Insufficient data for {city_name}. Skipping.")
        continue

    # Create the Price-to-Rent Ratio as the target variable
    city_data['Price-to-Rent Ratio'] = city_data['Median Home Value'] / city_data['Median Rent']
    
    # Drop any rows with missing values in the Price-to-Rent Ratio
    city_data = city_data.dropna(subset=['Price-to-Rent Ratio'])

    # Select the refined set of features
    features = city_data[['Median Home Value', 'Median Household Income', 
                          'Labor Force Participation', 'Educational Attainment (Total)']]
    
    # Check if enough rows remain after dropping NAs
    if len(features) < 3:
        print(f"Insufficient data after filtering features for {city_name}. Skipping.")
        continue
    
    # Standardize the features
    scaler = StandardScaler()
    standardized_features = scaler.fit_transform(features)
    
    # Standardize the target (Price-to-Rent Ratio)
    target = pd.Series(
        scaler.fit_transform(city_data[['Price-to-Rent Ratio']]).flatten(), 
        name='Price-to-Rent Ratio'
    )

    # Split data into time-ordered train and test sets (80% train, 20% test)
    train_size = int(len(target) * 0.8)
    X_train, X_test = standardized_features[:train_size], standardized_features[train_size:]
    y_train, y_test = target[:train_size], target[train_size:]

    # Find the best (p, d, q) order
    best_mse = float("inf")
    best_order = None

    for order in param_grid:
        try:
            model = ARIMA(y_train, order=order)
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=len(y_test))
            mse = mean_squared_error(y_test, forecast)
            
            if mse < best_mse:
                best_mse = mse
                best_order = order
        except:
            continue

    # Train the final ARIMA model with the best order
    if best_order is not None:
        model = ARIMA(y_train, order=best_order)
        model_fit = model.fit()
        
        # Forecast for the length of the test set
        forecast = model_fit.forecast(steps=len(y_test))
        
        # Calculate the Mean Squared Error with the best parameters
        mse = mean_squared_error(y_test, forecast)
        results[city_name] = mse
        print(f"{city_name} - Best ARIMA order: {best_order}, MSE: {mse}")

        # Plotting the actual vs predicted values
        plt.figure(figsize=(12, 6))
        plt.plot(range(len(y_test)), y_test, label='Actual Price-to-Rent Ratio', color='blue')
        plt.plot(range(len(forecast)), forecast, label='Predicted Price-to-Rent Ratio', color='orange')
        plt.title(f'Actual vs Predicted Price-to-Rent Ratio for {city_name}')
        plt.xlabel('Time Steps')
        plt.ylabel('Price-to-Rent Ratio')
        plt.legend()
        plt.grid()
        
        # Save the plot in the visualization folder
        plt.savefig(f'{visualization_folder}/{city_name.replace(",", "").replace(" ", "_")}_actual_vs_predicted.png')
        plt.close()  # Close the plot to free memory
    
    else:
        print(f"No suitable ARIMA order found for {city_name}. Skipping.")

# Save the MSE results for each city to a CSV file for easy reference
results_df = pd.DataFrame(list(results.items()), columns=['City', 'MSE'])
results_df.to_csv('all_cities_price_to_rent_mse_results.csv', index=False)
print("MSE results saved to 'all_cities_price_to_rent_mse_results.csv'")