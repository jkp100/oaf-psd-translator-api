# Mocked Translator Service for testing
import requests

class MockTranslatorService:
    def __init__(self, api_url):
        self.api_url = api_url
        
    def translate_text(self, text_to_translate, source_lang, target_lang):
        return f'Mocked translation of "{text_to_translate}" from {source_lang} to {target_lang}'
