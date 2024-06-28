# Import necessary libraries for the script
import os  # For interacting with the operating system
import shutil  # For file operations like moving files
import sys  # Access to some variables used or maintained by the interpreter
import requests  # To make HTTP requests to a specified URL
import csv # For reading and writing CSV files

# Variable to store your API token for authentication
api_token = "V7IY-EbDa-LB85-NIk0-NBKq-cG" 

def get_image_metadata(image_path, custom_context):
    """
    Fetches metadata for an image using the PhotoTag.ai API.

    :param image_path: The path to the image file.
    :param custom_context: A string of custom context to improve API results.
    """
    # The URL of the API endpoint
    url = "https://server.phototag.ai/api/keywords"
    # Headers for the request, including the authorization token
    headers = {"Authorization": f"Bearer {api_token}"}
    # The payload of the request, including language, maximum keywords, and custom context
    payload = {
        "language": "en",
        "maxKeywords": 40,
        "customContext": custom_context
    }
    # Open the image file in binary mode and send the request
    with open(image_path, 'rb') as img_file:
        files = {"file": img_file}
        response = requests.post(url, headers=headers, data=payload, files=files)

    # If the request is successful (status code 200), process the data
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            # Extract the title, description, and keywords from the response
            title = data.get("title", "")
            description = data.get("description", "")
            keywords = data.get("keywords", [])
            # Log the fetched metadata
            print(f"Metadata fetched for image: {image_path}")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print(f"Keywords: {keywords}")
            return title, description, keywords
    else:
        # Log failure if the request was unsuccessful
        print(f"Failed to fetch metadata. Check your API token. Status code: {response.status_code}")
    return None, None, []



   
