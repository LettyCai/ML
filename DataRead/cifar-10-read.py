import tensorflow as tf
import os

#定义cifar的数据等命令行参数
FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("cifar_dir","./cifar10","文件的目录")
tf.app.flags.DEFINE_string("cifar_tfrecords","./tmp/cifar.tfrecords","存进tfrecords的文件")

class CifaRead(object):
    """
        完成读取二进制文件，写进tfrecords
    """
    def __init__(self,filelist):
        #文件列表
        self.file_list = filelist

        #定义读取的图片的一些属性
        self.height = 32
        self.width = 32
        self.channel = 3
        # 二进制文件每张图片的字节
        self.label_bytes = 1
        self.image_bytes = self.height * self.width * self.channel
        self.bytes = self.label_bytes + self.image_bytes


    def read_and_decode(self):
        #1、构造文件队列
        file_queue = tf.train.string_input_producer(self.file_list)

        #2、构造二进制文件读取器，读取内容，每个样本的字节数
        reader = tf.FixedLengthRecordReader(self.bytes)

        key,value = reader.read(file_queue)

        #3、解码内容,二进制文件内容的解码
        label_image = tf.decode_raw(value,tf.uint8)

        #4、分割图片和标签数据
        label = tf.cast(tf.slice(label_image,[0],[self.label_bytes]),tf.int32)
        image = tf.slice(label_image,[self.label_bytes],[self.image_bytes])

        #5、对图片的特征数据进行形状的改变 [3072]-> [32,32,3]
        image_reshap = tf.reshape(image,[self.height,self.width,self.channel])

        #6、批处理数据
        image_batch,label_batch = tf.train.batch([image_reshap,label],batch_size=10,num_threads=1,capacity=10)

        return image_batch,label_batch

    def write_to_tfrecords(self,image_batch,label_batch):
        """
        将图片的特征值和目标值存进tfrecords
        :param image_batch: 10张图片的特征值
        :param lable_bathc: 10张图片的目标值
        :return:
        """

        #1、构造一个tfrecords文件
        writer = tf.python_io.TFRecordWriter(FLAGS.cifar_tfrecords)

        #2、x循环将所有样本写进文件，每张图片样本都要构造一个example
        for i in range(10):
            #取出第i个图片数据的特征值和目标值
            image = image_batch[i].eval().tostring()
            label = label_batch[i].eval()[0]

            #构造一个样本的example
            example = tf.train.Example(features=tf.train.Features(feature={
                "image":tf.train.Feature(bytes_list=tf.train.BytesList(value=[image])),
                "label":tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
            }))

            #写入单独的样本
            writer.write(example.SerializeToString())

        #关闭
        writer.close()

        return None

    def read_from_tfrecords(self):
        #1、构造文件队列
        file_queue = tf.train.string_input_producer([FLAGS.cifar_tfrecords])

        #2、构造文件阅读器，读取内容example,value=一个样本的序列化example
        tf_reader = tf.TFRecordReader()
        key,value = tf_reader.read(file_queue)

        #3、解析example
        feachers = tf.parse_single_example(value,features={
            "image":tf.FixedLenFeature([],dtype=tf.string),
            "label":tf.FixedLenFeature([],tf.int64)
        })

        print(feachers["image"])

        #4、解码内容,如果读取的内容格式是string 类型的，需要解码,如果是int64,float32不需要解码
        image = tf.decode_raw(feachers["image"],tf.uint8)

        #固定图片的形状，方便于批处理
        image_reshape = tf.reshape(image,[32,32,3])

        label = feachers["label"]

        print(image_reshape,label)

        #进行批处理
        image_batch,label_batch =tf.train.batch([image_reshape,label],batch_size=10,num_threads=1,capacity=10)

        return image_batch,label_batch

if __name__=="__main__":

    # 获取文件列表
    filename = os.listdir(FLAGS.cifar_dir)

    # 组合文件目录和文件名
    filelist = [os.path.join(FLAGS.cifar_dir,file) for file in filename if file[-3:] == "bin"]

    print(filename,filelist)

    cf = CifaRead(filelist)
    #image_batch,label_batch = cf.read_and_decode()

    image_batch_read,label_batch_read = cf.read_from_tfrecords()


    with tf.Session() as sess :
        #定义一个线程协调器
        coord = tf.train.Coordinator()

        #开启读文件的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)

        #存进tfrecords文件
        print("开始存储")
        #
        #cf.write_to_tfrecords(image_batch,label_batch)
        #
        print("结束存储")
        #
        #打印读取的内容
        #print(sess.run([image_batch,label_batch]))
        #
        print(sess.run([image_batch_read, label_batch_read]))
        #回收子线程
        coord.request_stop()
        coord.join(threads)

