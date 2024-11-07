from census import Census
import pandas as pd

# Initialize the Census API client
api_key = 'f4af3e130cd42fe0f97a63e30c9272ed01764ce7'
c = Census(api_key)

# Define fields with variable codes to pull from the Census API
fields = [
    'NAME', 'B25077_001E', 'B25064_001E', 'B19013_001E', 'B01003_001E',
    'B15003_001E', 'B23025_005E', 'B25002_001E', 'B25002_002E',
    'B25002_003E', 'B25075_001E'
]

# Pull data for all places in Georgia for a specific year (e.g., 2022)
data = c.acs5.state_place(fields, state_fips='13', place='*', year=2022)

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Define a mapping from variable codes to descriptive column names
column_mapping = {
    'NAME': 'Place Name',
    'B25077_001E': 'Median Home Value',
    'B25064_001E': 'Median Rent',
    'B19013_001E': 'Median Household Income',
    'B01003_001E': 'Total Population',
    'B15003_001E': 'Educational Attainment (Total)',
    'B23025_005E': 'Labor Force Participation',
    'B25002_001E': 'Total Housing Units',
    'B25002_002E': 'Occupied Units',
    'B25002_003E': 'Vacant Units',
    'B25075_001E': 'Owner-Occupied Units'
}

# Rename columns in the DataFrame
df.rename(columns=column_mapping, inplace=True)

# Save the DataFrame to CSV
df.to_csv('georgia_census_data_2022.csv', index=False)
print("Data saved to 'georgia_census_data_2022.csv'")