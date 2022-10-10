'''
Translator service for the project
'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Load the required IBM Watson credentials and setup
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# Init the Watson Language Translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Setup the URL to the service
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    Return the English to French translation of the text contained
    in the argument 'english_text'
    '''
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation['translations'][0]['translation']


def french_to_english(french_text):
    '''
    Return the French to English translation of the text contained
    in the argument 'french_text'
    '''
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation['translations'][0]['translation']


if __name__ == '__main__':
    print(french_to_english("C'est fantastique"))
    print(english_to_french("It is fantastic"))
