from TranslatorService import TranslatorService, MockTranslatorService, APITranslatorService

def main():
    # Input for Translation
    text_to_translate = input("Enter the text to translate: ")
    source_language = input("Enter the source language code (e.g., en for English): ")
    target_language = input("Enter the target language code (e.g., fr for French): ")

    # Using MockTranslatorService
    mocked_service = MockTranslatorService()
    mocked_result = mocked_service.translate_text(text_to_translate, source_language, target_language)
    print(f"Text to Translate: {mocked_result}")

    # Using APITranslatorService
    api_service = APITranslatorService(api_url="https://libretranslate.de/translate")
    api_result = api_service.translate_text(text_to_translate, source_language, target_language)
    print(f"API Translation: {api_result}")

    # Original translation function usage
    translation_service = TranslatorService()
    translation = translation_service.translate_text(text_to_translate, source_language, target_language)

    print(f"\nOriginal: {text_to_translate}")
    print(f"Translation: {api_result}")

if __name__ == "__main__":
    main()



