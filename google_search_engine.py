import requests

def google_search(query, api_key, cse_id):
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
            for item in results['items']:
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print("\n")
        else:
            print("No results found for this query.")
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Example usage
api_key = "AIzaSyADbLPIcw4CyfdzMxU_IpeH7ykX2as8PeI"
cse_id = "14f96eeb00453444e"
query = "Georgia new corporate headquarters and expansions"

google_search(query, api_key, cse_id)