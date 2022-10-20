import unittest

from translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishtofrench("Hello"),"Bojour")
        self.assertEqual(englishtofrench(""),"")
        self.assertNotEqual(englishtofrench("hello"),"Bojour")

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("Hello"),"Bojour")
        self.assertEqual(frenchtoenglish(""),"")
        self.assertNotEqual(frenchtoenglish("bojour"),"Hello")

unittest.main()