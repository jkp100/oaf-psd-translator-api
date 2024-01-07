import requests
import json

#Create Translator Service
class TranslatorService:
    def __init__(self, api_url):
        self.api_url = api_url

    #function to Translate text refering to API
    def translate_text(self, original_text, source_lang, target_lang):
        api_url = f"{self.api_url}/translate"
        headers = {"Content-Type": "application/json"}
        payload = {
            "q": original_text,
            "source": source_lang,
            "target": target_lang,
            "format": "text",
            "api_key": ""
        }

        response = requests.post(api_url, data=json.dumps(payload), headers=headers)
        
        #If statement for error handling displaying status codes in API
        if response.status_code == 200:
            result = response.json()
            print(result)
            return result["translatedText"]
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
