import requests
import json  # To pretty-print the JSON response

# Define your API key
api_key = 'f4af3e130cd42fe0f97a63e30c9272ed01764ce7'

# Define the base URL and parameters for the API request
state_fips = '13'  # FIPS code for Georgia
place_code = '37816'  # Place code for Atlanta
url = f'https://api.census.gov/data/2022/acs/acs5?get=NAME,B25077_001E,B25064_001E,B19013_001E&for=place:{place_code}&in=state:{state_fips}&key={api_key}'

# Make the request and get the response
response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:
    # Print the raw JSON data (prettified)
    data = response.json()
    print(json.dumps(data, indent=4))  # Pretty-print the JSON with indentation
else:
    print(f'Error: {response.status_code}')