import os
import re

import requests
from dotenv import load_dotenv


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


OPENAI_URL = "https://api.together.xyz/v1/chat/completions"


def get_together_answer(query):
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}

    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7,
    }

    try:
        response = requests.post(OPENAI_URL, json=data, headers=headers)
        response.raise_for_status()
        response_json = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None, None
    except ValueError as e:
        print(f"Error decoding JSON response: {e}")
        return None, None

    
    answer_text = (
        response_json.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
    )

    
    match = re.search(r"\b([1-9]|10)\b", answer_text)
    answer = int(match.group(1)) if match else None

    return answer, answer_text
