import sys
sys.path.append('../')

from credencial_apykey import *
import json

from ibm_watson import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey=visualrecognition_apikey)

#desabilita SSL
#visual_recognition.disable_SSL_verification()

with open('../../../datasets/imagens/lions/imagem_test1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='default').get_result()
print(json.dumps(classes, indent=2))

