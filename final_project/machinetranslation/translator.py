"""
translator.py

This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator


def english_to_french(text):
    """
    Translates English text to French.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text in French.
    """
    translator = MyMemoryTranslator(source='en', target='fr')
    translation = translator.translate(text)
    return translation


def french_to_english(text):
    """
    Translates French text to English.
    Args:
        text (str): The text to be translated.
    Returns:
        str: The translated text in English.
    """
    translator = MyMemoryTranslator(source='fr', target='en')
    translation = translator.translate(text)
    return translation

