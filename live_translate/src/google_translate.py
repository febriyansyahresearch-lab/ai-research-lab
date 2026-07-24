"""Google Translate provider using deep-translator."""

from .translator import Translator, TranslatorFactory

try:
    from deep_translator import GoogleTranslator as _GoogleTranslator
    _HAS_DEEP = True
except ImportError:
    _HAS_DEEP = False


class GoogleTranslateTranslator(Translator):
    def __init__(self):
        if not _HAS_DEEP:
            raise ImportError("deep-translator is required. Install with: pip install deep-translator")

    def translate(self, text, source='auto', target='en'):
        if not text.strip():
            return ""
        try:
            result = _GoogleTranslator(source=source, target=target).translate(text)
            return result or ""
        except Exception as e:
            raise RuntimeError(f"Google Translate error: {e}")


TranslatorFactory.register('google', GoogleTranslateTranslator)
