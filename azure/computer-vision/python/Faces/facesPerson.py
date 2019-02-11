import cognitive_face as CF
SUBSCRIPTION_KEY = ''
BASE_URL = 'https://centralus.api.cognitive.microsoft.com/face/v1.0/'
PERSON_GROUP_ID = 'known-persons'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)


CF.person_group.create(PERSON_GROUP_ID, 'Known Persons')


name = "Clemens Siebler"
user_data = 'More information can go here'
response = CF.person.create(PERSON_GROUP_ID, name, user_data)

# Get person_id from response
person_id = response['personId']

CF.person.add_face('clemens.jpg', PERSON_GROUP_ID, person_id)

print CF.person.lists(PERSON_GROUP_ID)

CF.person_group.train(PERSON_GROUP_ID)

response = CF.face.detect('test.jpg')
face_ids = [d['faceId'] for d in response]
print face_ids

identified_faces = CF.face.identify(face_ids, PERSON_GROUP_ID)
print identified_faces

