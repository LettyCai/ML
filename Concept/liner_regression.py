import tensorflow as tf
import os

def myregression():
    """
    自实现一个线性回归预测
    :return: None
    """
    #1、准备数据 ，x 特征值[100,1]  y 目标值 [100]



    x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name="x_data")

    #矩阵相乘必须是二维的
    y_true = tf.matmul(x,[[0.7]]) + 0.8

    #2、建立线性回归模型 1个特征，1个权重，1个偏置
    #随机给一个权重和偏置的值，计算损失，在当前状态下优化
    #trainable参数：指定这个变量能跟着梯度下降一起优化
    weight = tf.Variable(tf.random_normal([1,1],mean=0.0,stddev=1.0),name="w")
    bias = tf.Variable(0.0,name="b")

    y_predict = tf.matmul(x,weight) + bias

    #3、建立损失函数，均方误差
    loss = tf.reduce_mean(tf.square(y_true - y_predict))

    #4、梯度下降优化损失 learning_rate :0~1
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

    #收集tensor,
    tf.summary.scalar("losses",loss)
    tf.summary.histogram("weights",weight)
    #合并变量写入事件文件
    merged = tf.summary.merge_all()

    #定义一个初始化变量的op
    init_op = tf.global_variables_initializer()

    #定义一个保存模型的示例
    saver = tf.train.Saver()

    #通过会话运行程序
    with tf.Session() as sess:
        # 初始化变量
        sess.run(init_op)

        #打印随机初始化的偏置和权重
        print("随机初始化的参数权重为：%f ，偏置为：%f" % (weight.eval() ,bias.eval()))

        #加载模型，覆盖模型当中随机定义的参数,从上次训练的参数结果开始
        if os.path.exists('./ckpt/checkpoint'):
            saver.restore(sess,'./ckpt/model')


        #循环训练 运行优化
        for i in range(100):
            sess.run(train_op)
            print("第 %d 次优化的参数权重为：%f ，偏置为：%f" % (i,weight.eval() ,bias.eval()))

            #建立事件文件
            filewriter = tf.summary.FileWriter('./test/',graph=sess.graph)

            #运行合并的tensor
            summary = sess.run(merged)
            filewriter.add_summary(summary,i)

        saver.save(sess,"./ckpt/model")

    return None






if __name__ == "__main__":
    myregression()
