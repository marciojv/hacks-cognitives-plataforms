import tensorflow as tf

a=tf.add(3,5)

print(a)

sess=tf.Session()

print sess.run(a)

