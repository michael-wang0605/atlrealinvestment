import csv

# Open and read the national_places.txt file with 'latin1' encoding
with open('fipcodes_bystate.txt', 'r', encoding='latin1') as file:
    data = file.readlines()

# Filter out header lines if there are any, and extract Georgia-related lines
georgia_places = []
for line in data:
    parts = line.strip().split('|')  # Split each line by '|'
    
    # Check if the line is for Georgia (state FIPS code is 'GA')
    if parts[0] == 'GA':  # The first field is the state code (GA for Georgia)
        place_fips = parts[2]  # Place FIPS code
        place_name = parts[3]  # Place name
        place_county = parts[6]  # Place county
        
        # Ensure FIPS code is treated as a string to preserve leading zeros
        georgia_places.append((str(place_fips), str(place_name), str(place_county)))

# Write the results to a CSV file, ensuring all fields are treated as strings
with open('georgia_fipcodes.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header
    csvwriter.writerow(['FIPS Code', 'Place Name', 'County'])
    
    # Write the rows of data
    for place in georgia_places:
        csvwriter.writerow(place)

# Optionally print a success message
print("Data has been exported to 'georgia_fipcodes.csv' with leading zeros preserved.")