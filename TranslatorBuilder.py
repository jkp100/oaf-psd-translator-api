from TranslatorService import TranslatorService
from TranslatorHandler import TranslatorHandler

#Builder that create instances of TranslatorService and TranslatorHandler
class TranslatorBuilder:
    def build_service(self, api_url):
        return TranslatorService(api_url)

    def build_handler(self, translator_service):
        return TranslatorHandler(translator_service)
