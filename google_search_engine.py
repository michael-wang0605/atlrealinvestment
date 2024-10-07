import requests
import csv

# This list will store the results
url_list = []

# Function to search and save results
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
            # Open the CSV file in write mode
            with open(output_csv_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(['Link'])
                
                # Write each result to the CSV
                for item in results['items']:
                    link = item['link']
                    print(f"Link: {link}")
                    print("\n")
                    
                    # Append to list (optional)
                    url_list.append({'link': link})
                    
                    # Write the title and link to the CSV file
                    writer.writerow([link])
            
            print(f"Results saved to {output_csv_file}")
        else:
            print("No results found for this query.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Example usage
api_key = "AIzaSyADbLPIcw4CyfdzMxU_IpeH7ykX2as8PeI"
cse_id = "14f96eeb00453444e"
query = "Georgia new corporate headquarters and expansions"
output_csv_file = "search_results.csv"

google_search(query, api_key, cse_id, output_csv_file)