"""Tests for mock translator."""

from live_translate.src.mock import MockTranslator


def test_translate_returns_string():
    t = MockTranslator()
    result = t.translate('hello', 'en', 'id')
    assert isinstance(result, str)


def test_translate_includes_language_tags():
    t = MockTranslator()
    result = t.translate('hello', 'en', 'id')
    assert '[en→id]' in result


def test_translate_with_mapping():
    mapping = {'hello': 'halo', 'world': 'dunia'}
    t = MockTranslator(mapping)
    assert t.translate('hello') == 'halo'
    assert t.translate('world', 'en', 'id') == 'dunia'


def test_translate_empty_text():
    t = MockTranslator()
    result = t.translate('', 'en', 'id')
    assert '[en→id]' in result


def test_mock_provider_registered():
    from live_translate.src.translator import TranslatorFactory
    providers = TranslatorFactory.list_providers()
    assert 'mock' in providers
