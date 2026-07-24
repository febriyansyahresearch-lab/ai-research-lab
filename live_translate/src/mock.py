"""Mock translator for testing and offline use."""

from .translator import Translator, TranslatorFactory


class MockTranslator(Translator):
    def __init__(self, mapping=None):
        self.mapping = mapping or {}

    def translate(self, text, source='auto', target='en'):
        if text in self.mapping:
            return self.mapping[text]
        return f"[{source}→{target}] {text}"


TranslatorFactory.register('mock', MockTranslator)
