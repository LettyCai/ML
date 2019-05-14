import tensorflow as tf


g = tf.Graph()

print(g)

with g.as_default():
    c = tf.constant(11.0)
    print(c.graph)

a = tf.constant(5.0)
b = tf.constant(6.0)

sum1 = tf.add(a,b)

graph = tf.get_default_graph()

print(graph)

#有重载的机制，默认会给运算符重载成op类型
var1 = 2.0
sum2 = a + var1

#只能运行一个图，可以在会话当中指定图运行
#只要有会话的上下文环境，就可以使用eval()

#实时提供数据
#placeholder是一个占位符,feed_dict是一个字典
plt = tf.placeholder(tf.float32,[None,3])

with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(sess.run([a,b,sum1]))
    print(a.eval())
    print(sum1.graph)
    print(sess.graph)

    print(sess.run(plt,feed_dict={plt:[[1,2,3],[4,5,6]]}))

    print('*'*20)

    print(a.graph)
    print(a.shape)
    print(a.name)
    print(a.op)

#tensorflow：打印出来的形状表示
#0维：() 1维：(5) 2维：(2,3)

