import unittest
from machinetranslation import translator
class TestTranslatingMethods(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench(" ") == " ")
        self.assertEqual(translator.englishToFrench("Hello") == "Bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(translator.frenchToEnglish(" ") == " ")
        self.assertEqual(translator.frenchToEnglish("Bonjour") == "Hello")

if __name__ == '__main__':
    unittest.main()