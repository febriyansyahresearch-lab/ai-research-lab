"""Tests for Gemini translator provider."""

import os
from live_translate.src.gemini import GeminiTranslator, _PROMPT_TEMPLATE


def test_gemini_provider_registered():
    from live_translate.src.translator import TranslatorFactory
    providers = TranslatorFactory.list_providers()
    assert 'gemini' in providers


def test_prompt_template_format():
    prompt = _PROMPT_TEMPLATE.format(source='en', target='id', text='Hello')
    assert 'en' in prompt
    assert 'id' in prompt
    assert 'Hello' in prompt


def test_gemini_no_api_key_raises():
    saved = os.environ.pop('GEMINI_API_KEY', None)
    try:
        GeminiTranslator(api_key=None)
        assert False, "Should raise ValueError"
    except ValueError as e:
        assert 'API key' in str(e)
    except ImportError:
        pass
    finally:
        if saved is not None:
            os.environ['GEMINI_API_KEY'] = saved
