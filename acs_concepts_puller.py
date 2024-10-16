import requests
from bs4 import BeautifulSoup
import csv

# Step 1: Fetch the HTML content from the URL
url = "https://api.census.gov/data/2020/acs/acs5/variables.html"
response = requests.get(url)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Define a list to store concepts in order
concepts = []

# Step 4: Find all the table rows ('tr') and extract every third 'td' (concept)
rows = soup.find_all('tr')

for row in rows:
    cells = row.find_all('td')
    if len(cells) >= 3:
        concept = cells[2].get_text(strip=True)
        concepts.append(concept)  # Append to list to maintain order

# Step 5: Eliminate repeated concepts while preserving order
# Convert the list to a dict, then back to a list to remove duplicates but keep order
unique_concepts = list(dict.fromkeys(concepts))

# Step 6: Write the unique ordered concepts to a CSV file
with open('unique_ordered_concepts.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for concept in unique_concepts:
        writer.writerow([concept])

# Step 7: Print the first few unique concepts to verify (Optional)
print("First 10 unique concepts:", unique_concepts[:10])