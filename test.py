import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "https://api.census.gov/data/2020/acs/acs5/variables.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract unique concepts (without variable names)
concepts = set()  # Using a set to remove duplicates
table = soup.find('table')

for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) >= 3:
        concepts.add(cells[2].get_text(strip=True))

# Save the unique concepts to a file

print(concepts)