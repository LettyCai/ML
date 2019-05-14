import tensorflow as tf
import os

#批处理大小，跟队列，数据的数量没有关系，只决定这批次取多少数据，可能会重复
def csvread(filelist):
    """
    读取csv文件
    :param filelies: 文件路径列表
    :return: 读取的内容
    """
    #1、构造文件队列
    file_queue = tf.train.string_input_producer(filelist)

    #2、构造csv阅读器，读取队列数据
    reader = tf.TextLineReader()

    #读取内容
    key,value = reader.read(file_queue)

    #3、对每行内容解码
    #record_defaults：指定每一个样本每一列的类型，指定默认值
    records = [["None"],["None"]]
    example, lable = tf.decode_csv(value,record_defaults=records)

    print(example,lable)

    #4、想要读取多个数据，需要批处理
    example_bathc,lable_batch = tf.train.batch([example,lable],batch_size=9,num_threads=1,capacity=9)


    return example_bathc,lable_batch

if __name__ == "__main__":
    #找到文件，放入列表  路径+名字
    file_name = os.listdir("./csvdata/")

    filelist = [os.path.join("./csvdata/",file) for file in file_name]

    csvread(filelist)

    example,lable = csvread(filelist)

    #开启会话运行结果
    with tf.Session() as sess:
        #定义一个线程协调器
        coord = tf.train.Coordinator()

        #开启读取文件的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        #打印读取的内容
        print(sess.run([example,lable]))

        #回收子线程
        coord.request_stop()
        coord.join(threads)
