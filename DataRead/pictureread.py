import tensorflow as tf
import os
def readpic_decode(file_list):
    """
    批量读取图片并转换成张量格式
    :param file_list: 文件名目录列表
    :return: None
    """

    # 构造文件队列
    file_queue = tf.train.string_input_producer(file_list)

    # 图片阅读器和读取数据
    reader = tf.WholeFileReader()
    key,value = reader.read(file_queue)

    # 解码成张量形式

    image_first = tf.image.decode_jpeg(value)

    print(image_first)

    # 缩小图片到指定长宽，不用指定通道数
    image = tf.image.resize_images(image_first,[256,256])

    # 设置图片的静态形状,进行批处理的时候要求所有数据形状必须定义
    image.set_shape([256,256,3])

    print(image)

    # 批处理图片数据，tensors是需要具体的形状大小
    image_batch = tf.train.batch([image],batch_size=100,num_threads=1,capacity=100)

    tf.summary.image("pic",image_batch)

    with tf.Session() as sess:

        merged = tf.summary.merge_all()

        filewriter = tf.summary.FileWriter("/tmp/summary/dog/",graph=sess.graph)

        # 线程协调器
        coord = tf.train.Coordinator()

        # 开启线程
        threads = tf.train.start_queue_runners(sess=sess,coord=coord)

        print(sess.run(image_batch))

        summary = sess.run(merged)

        filewriter.add_summary(summary)

        # 等待线程回收
        coord.request_stop()
        coord.join(threads)


    return None


if __name__=="__main__":

    # 获取文件列表
    filename = os.listdir("./dog/")

    # 组合文件目录和文件名
    file_list = [os.path.join("./dog/",file) for file in filename]

    # 调用读取函数
    readpic_decode(file_list)