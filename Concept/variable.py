import tensorflow as tf

a = tf.constant(3.0,name="a")
b = tf.constant(4.0,name="b")
c = tf.add(a,b)

var = tf.Variable(tf.random_normal([2,3],mean=0.0,stddev=1.0))

print(a,var)

#必须显式初始化
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    #必须运行初始化op操作
    sess.run(init_op)
    print(sess.run([c,var]))

    #把程序的图结构写入事件文件,graph:把指定的图写进事件文件当中
    fillwriter = tf.summary.FileWriter("./test",graph=sess.graph)

