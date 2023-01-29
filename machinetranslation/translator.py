""" This module is intended to translate French to English and vice-versa"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Authentication
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def get_translator_models(source_lang, target_lang):
    """Function to get all the models"""
    return language_translator.list_models(source=source_lang, target=target_lang).get_result()

def english_to_french(english_text):
     """ French <- English """

     model = get_translator_models("en", "fr")
     french_text = language_translator.translate(
     text=english_text,
     model_id=model["models"][0]["model_id"]).get_result()
     return french_text["translations"][0]["translation"]

def french_to_english(french_text):
    """ French -> English """

    model = get_translator_models("fr", "en")
    english_text = language_translator.translate(
    text=french_text,
    model_id=model["models"][0]["model_id"]).get_result()
    return english_text["translations"][0]["translation"]

frenchText = english_to_french("Hello")
print(frenchText)
