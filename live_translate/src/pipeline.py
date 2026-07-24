"""Live translation pipeline with provider selection and fallback."""

from .translator import TranslatorFactory


class TranslationPipeline:
    def __init__(self, primary='google', fallback='mock', **kwargs):
        self.primary_name = primary
        self.fallback_name = fallback
        self.providers = {}
        try:
            self.providers[primary] = TranslatorFactory.create(primary, **kwargs.pop(primary, {}))
        except Exception:
            pass
        if fallback and fallback != primary:
            try:
                self.providers[fallback] = TranslatorFactory.create(fallback)
            except Exception:
                pass

    def translate(self, text, source='auto', target='en', provider=None):
        name = provider or self.primary_name
        if name in self.providers:
            try:
                return self.providers[name].translate(text, source, target)
            except Exception:
                if self.fallback_name and self.fallback_name in self.providers:
                    return self.providers[self.fallback_name].translate(text, source, target)
                raise
        raise ValueError(f"Provider '{name}' not initialized")

    def list_available(self):
        return list(self.providers.keys())
