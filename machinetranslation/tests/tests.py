import unittest
from machinetranslation import translator
class TestTranslatingMethods(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.english_to_french(" ")," ")
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(translator.french_to_english(" "), " ")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()