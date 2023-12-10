from TranslatorService import TranslatorService
from MockTranslatorService import MockTranslatorService
from TranslatorHandler import TranslatorHandler
from TranslatorDatabase import TranslatorDatabase
from TranslatorSentiment import TranslatorSentiment


if __name__ == "__main__":
    # Define API URLs for specific functions
    api_url = "https://libretranslate.de"

    # Test TranslatorService
    translator_service = TranslatorService(api_url)
    translator_service.translate_text("Enter text to be Translated to Spanish:")

    # Get user input for the original text
    original_text = input("Enter sample text to determine your language: ")

    # Create instances of TranslatorHandler with corresponding services
    translator_handler = TranslatorHandler(translator_service)

    # Test with LibreTranslate API service - Translate Text
    print("\nTesting with LibreTranslate API service - Translate Text:")
    text_to_translate = input("Enter text to be Translated to Spanish:")
    translated_text = translator_service.translate_text(text_to_translate)

    # Create a database object
    db = TranslatorDatabase()

    # Add a translation to the database
    source_lang = "auto"
    target_lang = "es"

    db.add_translation(original_text=original_text, detected_language=source_lang, translated_text=translated_text, source_lang=source_lang, target_lang=target_lang)

    # Retrieve and print Translation data
    translations = db.get_all_translations()
    print(translations)

    #Add Sentient Analyzer instance
    
    sentiment_analyzer = TranslatorSentiment()
    sentiment_score, sentiment_label = sentiment_analyzer.analyze_sentiment(translated_text)

    print(f"Sentiment Score: {sentiment_score}")
    print(f"Sentiment Label: {sentiment_label}")



