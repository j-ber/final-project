import unittest
from translator import translate_english_to_french, translate_french_to_english

class TranslationTestCase(unittest.TestCase):
    """
    Test case for translation methods.
    """

    def test_translate_english_to_french(self):
        """
        Test translation from English to French.
        """
        # Test translation of 'Hello'
        english_text = 'Hello'
        expected_french_translation = 'Bonjour'
        actual_french_translation = translate_english_to_french(english_text)
        self.assertEqual(actual_french_translation, expected_french_translation)

        # Test translation of 'Goodbye'
        english_text = 'Goodbye'
        expected_french_translation = 'Au revoir'
        actual_french_translation = translate_english_to_french(english_text)
        self.assertEqual(actual_french_translation, expected_french_translation)

    def test_translate_french_to_english(self):
        """
        Test translation from French to English.
        """
        # Test translation of 'Bonjour'
        french_text = 'Bonjour'
        expected_english_translation = 'Hello'
        actual_english_translation = translate_french_to_english(french_text)
        self.assertEqual(actual_english_translation, expected_english_translation)

        # Test translation of 'Merci'
        french_text = 'Merci'
        expected_english_translation = 'Thank you'
        actual_english_translation = translate_french_to_english(french_text)
        self.assertEqual(actual_english_translation, expected_english_translation)

if __name__ == '__main__':
    unittest.main()
