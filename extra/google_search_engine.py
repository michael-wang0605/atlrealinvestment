import requests
import csv

# Set to track already seen links
seen_links = set()

# Function to perform Google search and save results
def google_search(query, api_key, cse_id, output_csv_file):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": api_key,
        "cx": cse_id
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        results = response.json()
        
        if 'items' in results:
            # Open the CSV file in append mode to add results from multiple queries
            with open(output_csv_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write results for the current query
                for item in results['items']:
                    title = item['title']
                    link = item['link']
                    
                    # Check if the link is already in the seen_links set
                    if link not in seen_links:
                        # If the link is new, add it to the set and write it to the CSV
                        seen_links.add(link)
                        print(f"Title: {title}")
                        print(f"Link: {link}")
                        print("\n")
                        
                        # Write the query, title, and link to the CSV file
                        writer.writerow([query, title, link])
            
            print(f"Results for '{query}' saved to {output_csv_file}")
        else:
            print(f"No results found for '{query}'.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Example usage
api_key = "AIzaSyADbLPIcw4CyfdzMxU_IpeH7ykX2as8PeI"
cse_id = "14f96eeb00453444e"
output_csv_file = "search_results.csv"

# List of queries to search
queries = [
    "Georgia new corporate headquarters and expansions 2024",
    "new georgia startup developments 2024",
    "Construction news in georgia",
    "upcoming corporate and infrastructure developments in georgia 2024",
    "major construction projects and business expansions in georgia 2024",
    "Georgia city planning and transportation projects news 2024",
    "New park and public space developments in Georgia cities",
    "Georgia public infrastructure projects and transit expansions",
    "New construction and urban development in Georgia cities",
    "Atlanta metro area real estate and city development updates",
    "Public works, corporate projects, and city planning in Georgia 2024"
]

# Write the header to the CSV file before starting the search
with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Query', 'Title', 'Link'])

# Loop through the list of queries and perform the search for each
for query in queries:
    google_search(query, api_key, cse_id, output_csv_file)