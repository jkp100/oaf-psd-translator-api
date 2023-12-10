import requests
import json

class TranslatorService:
    def __init__(self, api_url):
        self.api_url = api_url

    def translate_text(self, original_text):
        api_url = f"{self.api_url}/translate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "q": original_text,
            "source": "auto",
            "target": "es",
            "format": "text",
            "api_key": ""
        }

        response = requests.post(api_url, data=json.dumps(payload), headers=headers)

        if response.status_code == 200:
            result = response.json()
            print(result)
            return result["translatedText"]
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
