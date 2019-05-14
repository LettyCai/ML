import tensorflow as tf

#静态形状和动态形状
#对于静态形状来说，一旦张量形状固定了，就不能再次设置，不能跨维度修改
#动态形状可以创建一个新的张量，元素数量要匹配，可以跨维度

plt = tf.placeholder(tf.float32,[None,2])
print(plt)
plt.set_shape([3,2])
print(plt)
#plt._set_shape([2,2]) 不能再修改

plt_reshape = tf.reshape(plt,[2,3])

print(plt_reshape)

zero = tf.zeros([3,4],tf.float32)
one = tf.ones([3,4],tf.float32)

with tf.Session() as sess:
    print(zero.eval())
    print(one.eval())
