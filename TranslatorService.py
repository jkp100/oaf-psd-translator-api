import requests

def translate_text(text, source_lang, target_lang):
    api_url = "https://libretranslate.de/translate"
    
    params = {
        'q': text,
        'source': source_lang,
        'target': target_lang
    }

    response = requests.post(api_url, data=params)

    if response.status_code == 200:
        translation = response.json()['translatedText']
        return translation
    else:
        return f"Error {response.status_code}: {response.text}"

# Example usage
text_to_translate = "Hello, how are you?"
source_language = "en"
target_language = "fr"

result = translate_text(text_to_translate, source_language, target_language)
print(f"Original: {text_to_translate}")
print(f"Translation: {result}")
