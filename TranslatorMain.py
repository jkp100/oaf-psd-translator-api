from TranslatorService import TranslatorService
from TranslatorHandler import TranslatorHandler
from TranslatorDatabase import TranslatorDatabase
from TranslatorSentiment import TranslatorSentiment


#Function to prompt user for input
def get_user_input(prompt):
    return input(prompt)

#Function to reset database
def reset_database(db):

    # Ask the user if they want to reset the database
    reset_confirmation = get_user_input("\nDo you want to reset past conversations? (yes/no): ").lower()

    if reset_confirmation == "yes":
        db.reset_database()
        print("Conversation reset successfully.")
    else:
        print("Conversation not reset.")

def main():
    # Define API URLs for specific functions
    api_url = "https://libretranslate.de"

    # Test TranslatorService
    translator_service = TranslatorService(api_url)
    
    # Create instance of TranslatorHandler with TranslatorService
    translator_handler = TranslatorHandler(translator_service)

    # Get user input for the original text
    original_text = get_user_input("Enter sample text to determine your current language: ")

    #Auto-Detect Source Language
    source_lang = "auto"


    #Call get_target_language from TranslatorHandler to set target language to translate to
    target_lang = translator_handler.get_target_language()

    # Test with LibreTranslate API service - Translate Text
    print(f"\nTesting with LibreTranslate API service - Translate Text Results:{source_lang}")
    text_to_translate = get_user_input(f"Enter text to be Translated to {target_lang}:")


    # Translate user text using TranslatorHandler
    translated_text = translator_handler.translate_text(text_to_translate, source_lang, target_lang)

    # Create a database object
    db = TranslatorDatabase()

    # Add a translation to the database
    conversation = (text_to_translate, source_lang, translated_text, target_lang)
    db.add_translation(conversation)

    # Add Sentiment Analyzer instance
    sentiment_analyzer = TranslatorSentiment()
    sentiment_score, sentiment_label = sentiment_analyzer.analyze_sentiment(text_to_translate)

 
    # Display Original & Translated Text
    print(f"\nOriginal Text: {text_to_translate}")
    print(f"Translated Text: {translated_text}")
    
    # Display Sentiment Score and Label
    print(f"Sentiment Score: {sentiment_score}")
    print(f"Sentiment: {sentiment_label}")

    # Display Past Conversations
    display_past_conversations = get_user_input("\nDo you want to display past conversations? (yes/no): ").lower()

    if display_past_conversations == "yes":

        translations = db.get_all_translations()
        
        #Checks if variable is not none: error handling for list of tuples
        if translations is not None:
            print("\nAll Past Translations:")
            for i, (original_text, translated_text) in enumerate(translations):
                print(f"Translation {i + 1}:")
                print(f"Original Text: {original_text}")
                print(f"Translated Text: {translated_text}")
                print()
        else:
            print("Error retrieving past translations.")
            

    # Asks user if they want to reset the database
    reset_database(db)


    db.close_connection()


if __name__ == "__main__":
    main()



