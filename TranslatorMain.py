from TranslatorBuilder import TranslatorBuilder
from MockTranslatorService import MockTranslatorService
from TranslatorService import TranslatorService
from TranslatorHandler import TranslatorHandler
from TranslatorDatabase import TranslatorDatabase  


if __name__ == "__main__":
    # Create instance TranslatorBuilder
    builder = TranslatorBuilder()

    # Define API URLs for specific functions
    api_base_url = "https://libretranslate.com"
    api_url_detect_lang = "https://libretranslate.com/detect"  # language detection
    api_url_get_lang = "https://libretranslate.com/languages"  # get supported languages
    api_url_translate_text = "https://libretranslate.com/translate"  # translate source text to target text

    # Create instances of TranslatorService with specified URLs
    translator_service_detect_lang = TranslatorService(api_url_detect_lang)
    translator_service_get_lang = TranslatorService(api_url_get_lang)
    translator_service_translate_text = TranslatorService(api_url_translate_text)

    # Create instances of TranslatorHandler with corresponding services
    translator_handler_detect_lang = TranslatorHandler(translator_service_detect_lang)
    translator_handler_get_lang = TranslatorHandler(translator_service_get_lang)
    translator_handler_translate_text = TranslatorHandler(translator_service_translate_text)

    # Test with LibreTranslate API service - Translate Text
    print("\nTesting with LibreTranslate API service - Translate Text:")
    translator_handler_translate_text.translate_text("en", "es")

    print("\nTesting with LibreTranslate API service - Get Supported Languages:")
    translator_handler_get_lang.get_lang()

    # Test with the mocked service
    mocked_service = MockTranslatorService(api_url_detect_lang, api_url_get_lang, api_url_translate_text)
    mocked_handler = builder.build_handler(mocked_service)
    print("\nTesting with mock service:")
    mocked_handler.translate_text(source_lang="en", target_lang="es")

    # Create a database object
    db = TranslatorDatabase()

    # Add a translation to the database
    db.add_translation("Hello", "en", "Hola", "en", "es")

    # Retrieve and print Translation data
    translations = db.get_all_translations()
    print(translations)












