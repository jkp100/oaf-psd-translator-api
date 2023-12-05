import requests

class TranslatorService:
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def detect_lang(self, text_to_translate):
        detect_url = f'{self.api_base_url}/detect'
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'q': text_to_translate}
        response = requests.post(detect_url, headers=headers, data=data)

        if response.status_code == 200:
            result = response.json()
            detected_language = result['language']
            return detected_language
        else:
            print(response.content) 
            return None  

    def get_lang(self):
        get_lang_url = f'{self.api_base_url}/languages'
        headers = {'accept': 'application/json'}
        response = requests.get(get_lang_url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            supported_languages = result['languages']
            return supported_languages
        else:
            print(response.content)
            return None  

    def translate_text(self, text_to_translate, source_lang, target_lang):
        translate_url = f'{self.api_base_url}/translate'
        headers = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'q': text_to_translate,
            'source': source_lang,
            'target': target_lang,
            'format': 'text'
        }
        response = requests.post(translate_url, headers=headers, data=data)

        if response.status_code == 200:
            result = response.json()
            translated_text = result['translatedText']
            return translated_text
        else:
            print(response.content)
            return None  # Return None for graceful handling


    





