import sys
sys.path.append('../')

from credencial_apykey import *
import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey=visualrecognition_apikey)

with open('/home/marcio/Downloads/turma_IA_FIAP.jpeg', 'rb') as images_file:
    faces = visual_recognition.detect_faces(images_file).get_result()
print(json.dumps(faces, indent=2))

