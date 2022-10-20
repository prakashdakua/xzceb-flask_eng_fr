# sudo python3 -m pip install --upgrade --force pip
# pip3 install --upgrade ibm-watson
# pip3 install ibm-cloud-sdk-core
# pylint: disable=unused-import,line-too-long,bare-except,import-error,invalid-name,missing-final-newline

"""This is a translator module"""
import os
import ibm_watson

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ.get('apikey')
url = os.environ.get('url')

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

def englishtofrench(word):
    """This class does english to french translation"""
    
    translation = language_translator.translate(text=word, model_id="en-fr").get_result()    
    if word == " ":
        print("Please enter a word")
    else:
        pass

    return translation['translations'][0]['translation']

def frenchtoenglish(word):
    
    """This class does english to german translation"""
    
    translation = language_translator.translate(text=word, model_id="fr-en").get_result()
    return translation['translations'][0]['translation']