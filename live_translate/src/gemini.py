"""Gemini AI translator using google-generativeai."""

import os
from .translator import Translator, TranslatorFactory

try:
    import google.generativeai as genai
    _HAS_GEMINI = True
except ImportError:
    _HAS_GEMINI = False


_PROMPT_TEMPLATE = (
    "Translate the following text from {source} to {target}. "
    "Respond with only the translated text, no explanations.\n\n{text}"
)


class GeminiTranslator(Translator):
    def __init__(self, model_name='gemini-2.0-flash', api_key=None):
        if not _HAS_GEMINI:
            raise ImportError("google-generativeai is required. Install with: pip install google-generativeai")
        self.model_name = model_name
        key = api_key or os.getenv('GEMINI_API_KEY')
        if not key:
            raise ValueError("Gemini API key required. Set GEMINI_API_KEY env var or pass api_key.")
        genai.configure(api_key=key)
        self._model = genai.GenerativeModel(model_name)

    def translate(self, text, source='auto', target='en'):
        if not text.strip():
            return ""
        prompt = _PROMPT_TEMPLATE.format(source=source, target=target, text=text)
        try:
            response = self._model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            raise RuntimeError(f"Gemini translation error: {e}")


TranslatorFactory.register('gemini', GeminiTranslator)
