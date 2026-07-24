"""Tests for Google Translate provider."""

from live_translate.src.google_translate import GoogleTranslateTranslator


def test_google_provider_registered():
    from live_translate.src.translator import TranslatorFactory
    providers = TranslatorFactory.list_providers()
    assert 'google' in providers


def test_google_translate_english():
    t = GoogleTranslateTranslator()
    result = t.translate('Hello', source='auto', target='id')
    assert isinstance(result, str)
    assert len(result) > 0


def test_google_translate_empty():
    t = GoogleTranslateTranslator()
    result = t.translate('', source='auto', target='en')
    assert result == ''


def test_google_translate_reverse():
    t = GoogleTranslateTranslator()
    id_result = t.translate('Good morning', 'auto', 'id')
    en_result = t.translate(id_result, 'auto', 'en')
    assert 'morning' in en_result.lower() or 'good' in en_result.lower()
