import sys
sys.path.append('../')

from credencial_apykey import *
import json

from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey=visualrecognition_apikey)

with open('../../../datasets/imagens/lions/imagem_test1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='default').get_result()
print(json.dumps(classes, indent=2))

