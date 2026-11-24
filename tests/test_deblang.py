import unittest
from deblang import DebTranslator

class TranslatorTests(unittest.TestCase):
    def setUp(self):
        self.translator = DebTranslator()

    def test_keywords(self):
        self.assertEqual(self.translator.translate('agar sach: bolo("hi")'),
                         'if True: print("hi")')

    def test_strings_are_not_translated(self):
        self.assertEqual(self.translator.translate('bolo("agar warna")'),
                         'print("agar warna")')

    def test_comments_are_not_translated(self):
        self.assertEqual(self.translator.translate('x = 1 # agar sach'),
                         'x = 1 # agar sach')

    def test_triple_string(self):
        source = 'text = """agar\\nwarna"""\nbolo(text)'
        self.assertEqual(self.translator.translate(source),
                         'text = """agar\\nwarna"""\nprint(text)')

if __name__ == "__main__":
    unittest.main()
