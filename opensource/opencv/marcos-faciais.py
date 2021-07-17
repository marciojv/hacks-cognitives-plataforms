import dlib
import cv2
import numpy
predictor_68_path = "haarcascade/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_68_path)
detector = dlib.get_frontal_face_detector()


def get_landmarks(im):
   rects = detector(im, 1)
   if len(rects) > 1:
   	raise Exception("Encontrado mais de uma face")
   if len(rects) == 0:
   	raise Exception("Sem face")
   return numpy.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])

def annotate_landmarks(im, landmarks):
	im = im.copy()
	for idx, point in enumerate(landmarks):
		pos = (point[0, 0], point[0, 1])
		cv2.putText(im, str(idx), pos,
		fontFace=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, fontScale=0.4,
		color=(0, 0, 255))
	cv2.circle(im, pos, 3, color=(0, 255, 255))
	return im

image = cv2.imread('dataset/silvio.jpg')
landmarks = get_landmarks(image)
image_with_landmarks = annotate_landmarks(image, landmarks)
cv2.imshow('Result', image_with_landmarks)
cv2.imwrite('results/silvio_landmarks.jpg',image_with_landmarks)
cv2.waitKey(0)
cv2.destroyAllWindows()
