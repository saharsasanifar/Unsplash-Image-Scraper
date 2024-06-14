import requests
import json

# Your Unsplash API access key
access_key = 'ndmCMyg2kGuyHLiOdq5-2UxAq-jqZMGtS8U3REFDN20'

def search_and_download_photo(query, filename):
    # Unsplash API endpoint
    search_url = "https://api.unsplash.com/search/photos"
    params = {
        'query': query,
        'client_id': access_key,
        'per_page': 1,
        'orientation': 'landscape'
    }

    response = requests.get(search_url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        if data['results']:
            # Get the URL of the first photo in the results
            photo_url = data['results'][0]['urls']['regular']
            download_photo(photo_url, filename)
        else:
            print("No photos found for the query.")
    else:
        print(f"Error occurred: {response.status_code}")
        print(response.text)

def download_photo(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"Photo saved as {filename}")
    else:
        print(f"Failed to download photo: {response.status_code}")

# Example usage
search_and_download_photo('nature', 'nature_photo.jpg')
