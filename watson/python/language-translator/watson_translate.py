import sys
sys.path.append('../')

from credencial_apykey import *
import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey=language_apikey,
    url='https://gateway-wdc.watsonplatform.net/language-translator/api')

translation = language_translator.translate(
    text='lion',
    model_id='en-pt').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))


translation = language_translator.translate(
    text='feline',
    model_id='en-pt').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))

