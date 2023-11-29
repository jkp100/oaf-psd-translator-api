import requests

class TranslatorService:
    def translate_text(self, text, source_lang, target_lang):
        pass
    
class MockTranslatorService(TranslatorService):
    def translate_text(self, text, source_lang, target_lang):
        # Mock implementation
        return f"Translating... '{text}' from {source_lang} to {target_lang}"

class APITranslatorService(TranslatorService):
    def __init__(self, api_url):
        self.api_url = api_url

    def translate_text(self, text, source_lang, target_lang):
        params = {
            'q': text,
            'source': source_lang,
            'target': target_lang
        }

        response = requests.post(self.api_url, data=params)

        if response.status_code == 200:
            translation = response.json()['translatedText']
            return translation
        else:
            return f"Error {response.status_code}: {response.text}"



