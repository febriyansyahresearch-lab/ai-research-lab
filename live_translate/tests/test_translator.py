"""Tests for translator interface and factory."""

from live_translate.src.translator import Translator, TranslatorFactory


class _ConcreteTranslator(Translator):
    def translate(self, text, source='auto', target='en'):
        return f"{text} [{source}→{target}]"


def test_base_class_cannot_instantiate():
    try:
        Translator()
        assert False, "Should raise TypeError"
    except TypeError:
        pass


def test_factory_register_and_create():
    TranslatorFactory.register('test_concrete', _ConcreteTranslator)
    t = TranslatorFactory.create('test_concrete')
    result = t.translate('hello', 'en', 'id')
    assert 'hello' in result
    assert 'en→id' in result


def test_factory_invalid_provider():
    try:
        TranslatorFactory.create('nonexistent')
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert 'nonexistent' in str(e)


def test_factory_list_providers():
    providers = TranslatorFactory.list_providers()
    assert 'mock' in providers
    assert 'test_concrete' in providers
