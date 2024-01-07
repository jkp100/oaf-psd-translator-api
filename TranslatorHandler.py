# Handler that interacts with TranslatorService
class TranslatorHandler:
    def __init__(self, translator_service):
        self.translator_service = translator_service

    #Function to get user input
    def get_user_input(self, prompt):
        return input(prompt)
    
    #Function to set target language
    def get_target_language(self):
        
        # Dictionary mapping names to language codes
        language_options = {
            "Espanol": "es",
            "Arabic": "ar",
            "Chinese": "zh",
            "English": "en",
            "French": "fr",
            "Hindi": "hi",
            "Japanese": "ja",
            "Thai": "th"
        }

        #Promt user to choose target language
        print("\nChoose a target language:")
        for name, code in language_options.items():
            print(f"{name} ({code})")

        # Validate the user input
        selected_language = ""
        while selected_language not in language_options.values():
            selected_language = self.get_user_input("Enter the language code for your target language: ")
            if selected_language not in language_options.values():
                print("Invalid language code. Please try again.")

        return selected_language
    
    
    #Function to translate text
    def translate_text(self, text_to_translate, source_lang, target_lang):
        try:
            translated_text = self.translator_service.translate_text(text_to_translate, source_lang, target_lang)
            print(f"Test Translation: {translated_text}")
            return translated_text
        except Exception as e:
            print(f"Error: {e}")



