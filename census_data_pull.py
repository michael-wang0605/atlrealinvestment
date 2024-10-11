import requests
import csv

# Define your API key
api_key = 'f4af3e130cd42fe0f97a63e30c9272ed01764ce7'

# Define the base URL for the Census API
base_url = 'https://api.census.gov/data/2020/acs/acs5'

# Open the CSV file with FIPS codes and prepare the output CSV file
with open('georgia_fipcodes.csv', 'r') as csvfile, open('georgia_census_data.csv', 'w', newline='') as outfile:
    csvreader = csv.reader(csvfile)
    csvwriter = csv.writer(outfile)
    
    # Write the header for the output file
    csvwriter.writerow(['Place Name', 'FIPS Code', 'Median Home Value', 'Median Rent', 'Median Household Income'])

    # Skip the header row in the input CSV
    next(csvreader)

    # Iterate through each row in the input CSV file
    for row in csvreader:
        place_name = row[1]  # Place name
        place_code = row[0]  # FIPS code (for the place)
        state_fips = '13'  # Georgia state FIPS code is '13'
        
        # Construct the API URL with the FIPS codes
        url = f'{base_url}?get=NAME,B25077_001E,B25064_001E,B19013_001E&for=place:{place_code}&in=state:{state_fips}&key={api_key}'
        
        # Make the request and get the response
        response = requests.get(url)
        
        # Check if the response was successful
        if response.status_code == 200:
            data = response.json()
            # Extract relevant data
            city = data[1][0]
            median_home_value = data[1][1] or 'N/A'
            median_rent = data[1][2] or 'N/A'
            median_income = data[1][3] or 'N/A'
            
            # Write the data to the output CSV file
            csvwriter.writerow([city, place_code, median_home_value, median_rent, median_income])
        else:
            print(f'Error: {response.status_code} for {place_name}')

print("Data has been exported to 'georgia_census_data.csv'.")