'''
Unit tests for the IBM Watson translator
'''
import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    '''
    Test Class for Translator service unit tests
    '''
    def test_null_english_to_french(self):
        '''
        Test for null input for english_to_french
        '''
        self.assertEqual(' ', english_to_french(' '))

    def test_null_french_to_english(self):
        '''
        Test for null input for french_to_english
        '''
        self.assertEqual(' ', french_to_english(' '))

    def test_hello_english_to_french(self):
        '''
        Test for translation of the word 'Hello' and 'Bonjour'
        '''
        self.assertEqual("Bonjour", english_to_french('Hello'))
        self.assertNotEqual("Salut", english_to_french('Hello'))

    def test_bonjour_french_to_english(self):
        '''
        Test for translation of the word 'Bonjour' and 'Hello'
        '''
        self.assertEqual('Hello', french_to_english('Bonjour'))
        self.assertNotEqual('How ya', french_to_english('Bonjour'))


if __name__ == '__main__':
    unittest.main()
