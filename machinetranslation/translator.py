import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Authentication
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#Function to get all the models
def getTranslatorModels(sourceLang , targetLang):
    return language_translator.list_models(source=sourceLang , target=targetLang).get_result()

#To convert from english to french
def englishToFrench(englishText):
    #write the code here
    model=getTranslatorModels("en","fr")
    frenchText = language_translator.translate(
    text=englishText,
    model_id=model["models"][0]["model_id"]).get_result()
    return frenchText["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    #write the code here
    model=getTranslatorModels("fr","en")
    englishText = language_translator.translate(
    text=frenchText,
    model_id=model["models"][0]["model_id"]).get_result()
    return englishText["translations"][0]["translation"]    

frenchText=englishToFrench(" ")
print(frenchText)