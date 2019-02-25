import tensorflow as tf

g=tf.Graph()

with g.as_default():
	x=tf.add(2,3)

sess=tf.Session(graph=g)

print sess.run(x)
