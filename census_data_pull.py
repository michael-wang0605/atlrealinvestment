from census import Census
import pandas as pd
from census import Census, CensusException

# Initialize the Census API client
api_key = 'f4af3e130cd42fe0f97a63e30c9272ed01764ce7'
c = Census(api_key)

# Define the initial list of fields with variable codes to pull from the Census API
fields = [
    'NAME', 'B25077_001E', 'B25064_001E', 'B19013_001E', 'B01003_001E',
    'B15003_001E', 'B23025_005E', 'B25002_001E', 'B25002_002E',
    'B25002_003E', 'B25075_001E'
]

# Define the range of years for which we want to pull data (e.g., 2010 to 2022)
years = range(2010, 2023)  # Adjust this range as needed

# Initialize an empty list to store data for all years
all_data = []

# Loop over each year and pull data
for year in years:
    try:
        # Pull data for all places in Georgia (state FIPS code 13) for the current year
        data = c.acs5.state_place(fields, state_fips='13', place='*', year=year)
        
        # Add the 'Year' key to each entry in the dataset
        for entry in data:
            entry['Year'] = year  # Add the year to each row
        
        # Append the year's data to the all_data list
        all_data.extend(data)
    except CensusException as e:
        # Log the error and print a message for the unavailable field
        print(f"Error retrieving data for year {year}: {e}")
        continue

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(all_data)

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
    'B25075_001E': 'Owner-Occupied Units',
    'Year': 'Year'
}

# Rename columns in the DataFrame
df.rename(columns=column_mapping, inplace=True)

# Save the DataFrame to a CSV file with data from all years
df.to_csv('georgia_census_data_all_years.csv', index=False)
print("Data for all specified years has been saved to 'georgia_census_data_all_years.csv'")