"""Abstract translator interface and provider factory."""

from abc import ABC, abstractmethod


class Translator(ABC):
    @abstractmethod
    def translate(self, text, source='auto', target='en'):
        pass


class TranslatorFactory:
    _providers = {}

    @classmethod
    def register(cls, name, provider_cls):
        cls._providers[name] = provider_cls

    @classmethod
    def create(cls, name, **kwargs):
        if name not in cls._providers:
            raise ValueError(f"Unknown provider: {name}. Available: {list(cls._providers.keys())}")
        return cls._providers[name](**kwargs)

    @classmethod
    def list_providers(cls):
        return list(cls._providers.keys())
