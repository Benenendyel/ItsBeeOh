import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.themoviedb.org/3/configuration"

# 1. Put your v3 API key into the query parameters dictionary
params = {"api_key": os.getenv("API_KEY")}

# 2. Optional: Keep the accept header for JSON format
headers = {"accept": "application/json"}

# 3. Pass params=params into requests.get()
response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    print("Success!")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
