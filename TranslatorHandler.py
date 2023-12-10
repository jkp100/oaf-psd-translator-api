# Handler that interacts with TranslatorService
class TranslatorHandler:
    def __init__(self, translator_service):
        self.translator_service = translator_service

    def detect_lang(self, text_to_translate):
        try:
            detected_language = self.translator_service.detect_lang(text_to_translate)
            print(f"Detected Language: {detected_language}")
        except Exception as e:
            print(f"Error: {e}")

    def get_lang(self):
        try:
            supported_languages = self.translator_service.get_lang()
            print(f"Supported Languages: {supported_languages}")
        except Exception as e:
            print(f"Error: {e}")

    def translate_text(self, source_lang, target_lang):
        text_to_translate = input("Enter the text to translate: ")
        try:
            translated_text = self.translator_service.translate_text(text_to_translate, source_lang, target_lang)
            print(f"Translation: {translated_text}")
        except Exception as e:
            print(f"Error: {e}")




