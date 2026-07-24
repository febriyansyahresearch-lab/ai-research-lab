"""Tests for translation pipeline."""

import os
from live_translate.src.pipeline import TranslationPipeline
from live_translate.src.translator import Translator, TranslatorFactory


def test_pipeline_with_mock():
    pipeline = TranslationPipeline(primary='mock')
    result = pipeline.translate('hello', 'en', 'id')
    assert '[en→id]' in result


def test_pipeline_different_languages():
    pipeline = TranslationPipeline(primary='mock')
    result = pipeline.translate('hello', 'en', 'ja')
    assert '[en→ja]' in result


def test_pipeline_empty_text():
    pipeline = TranslationPipeline(primary='mock')
    result = pipeline.translate('', 'en', 'id')
    assert isinstance(result, str)


def test_pipeline_list_available():
    pipeline = TranslationPipeline(primary='mock', fallback=None)
    available = pipeline.list_available()
    assert 'mock' in available


def test_pipeline_with_google_translate():
    pipeline = TranslationPipeline(primary='google', fallback='mock')
    result = pipeline.translate('Hello, how are you?', 'auto', 'id')
    assert isinstance(result, str)
    assert len(result) > 0


def test_pipeline_google_to_english():
    pipeline = TranslationPipeline(primary='google', fallback='mock')
    result = pipeline.translate('Bonjour le monde', 'auto', 'en')
    assert isinstance(result, str)
    assert len(result) > 0


def test_pipeline_uses_fallback_on_failure():
    class FailingTranslator(Translator):
        def translate(self, text, source='auto', target='en'):
            raise RuntimeError("Translation failed")

    TranslatorFactory.register('failing', FailingTranslator)
    pipeline = TranslationPipeline(primary='failing', fallback='mock')
    result = pipeline.translate('hello', 'en', 'id')
    assert result is not None
