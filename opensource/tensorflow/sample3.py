import tensorflow as tf

a=tf.constant([2.],dtype=tf.float32)
b=tf.constant([5.],dtype=tf.float32)
x=tf.placeholder(tf.float32)

y=a*x+b

sess=tf.Session()
print(sess.run(y,{x:[1,2,3,4]}))




