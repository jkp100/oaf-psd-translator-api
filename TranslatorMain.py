from TranslatorService import translate_text

def main():
    text_to_translate = input("Enter the text to translate: ")
    source_language = input("Enter the source language code (e.g., en for English): ")
    target_language = input("Enter the target language code (e.g., fr for French): ")

    translation = translate_text(text_to_translate, source_language, target_language)

    print(f"\nOriginal: {text_to_translate}")
    print(f"Translation: {translation}")

if __name__ == "__main__":
    main()



