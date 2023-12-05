# Mocked Translator Service for testing
import requests

class MockTranslatorService:
    def __init__(self, api_url_detect_lang, api_url_get_lang, api_url_translate_text):
        self.api_url_detect_lang = api_url_detect_lang
        self.api_url_get_lang = api_url_get_lang
        self.api_url_translate_text = api_url_translate_text

    def translate_text(self, text_to_translate, source_lang, target_lang):
        return f'Mocked translation of "{text_to_translate}" from {source_lang} to {target_lang}'