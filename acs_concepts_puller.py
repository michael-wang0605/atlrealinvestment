import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "https://api.census.gov/data/2020/acs/acs5/variables.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract unique concepts (without variable names)
concepts = set()  # Using a set to remove duplicates
for row in soup.select('tr'):
    cells = row.find_all('td')
    if len(cells) > 1:  # Ensures there is a concept in the row
        concept = cells[2].text.strip()  # Only get the concept (second column)
        concepts.add(concept)

# Save the unique concepts to a file
with open('unique_concepts.txt', 'w') as file:
    for concept in sorted(concepts):
        file.write(concept + '\n')

print("Unique concepts have been saved to unique_concepts.txt")
