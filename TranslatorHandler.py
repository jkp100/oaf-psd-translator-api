# Handler that interacts with TranslatorService
class TranslatorHandler:
    def __init__(self, translator_service):
        self.translator_service = translator_service

    def translate_text(self, source_lang, target_lang):
        text_to_translate = input("Enter text to translate: ")
        try:
            translated_text = self.translator_service.translate_text(text_to_translate, source_lang, target_lang)
            print(f"Translation: {translated_text}")
        except Exception as e:
            print(f"Error: {e}")




