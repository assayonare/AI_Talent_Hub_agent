import os

import requests
from dotenv import load_dotenv

# Load secret
load_dotenv()
SEARCH_API_KEY = os.getenv("SEARCH_API_KEY")

SEARCH_ENGINE_ID = "e31766b84d260454a"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1"


def search_web(query):
    params = {"q": query, "key": SEARCH_API_KEY, "cx": SEARCH_ENGINE_ID}
    response = requests.get(SEARCH_URL, params=params).json()
    links = [item["link"] for item in response.get("items", [])[:3]]
    return links
