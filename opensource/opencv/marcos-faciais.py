import dlib
import numpy
predictor_68_path = "../../models/shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_68_path)
detector = dlib.get_frontal_face_detector()
def get_landmarks(im):
   rects = detector(im, 1)
   if len(rects) > 1:
   	raise Exception("Encontrado mais de uma face")
   if len(rects) == 0:
   	raise Exception("Sem face")
   return numpy.matrix([[p.x, p.y] for p in predictor(im, rects[0]).parts()])
