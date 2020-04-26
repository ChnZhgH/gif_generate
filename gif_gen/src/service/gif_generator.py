import functools
import os
import imageio
import time

from .video_processor import VideoProcessor


class GifGenerator(object):
    def __init__(self):
        self.IMAGES_DIR = os.path.join(os.getcwd(), "tmp/images")

    def video2gif(self, video_path, gif_path):
        # 1. 清空临时文件夹
        file_names = os.listdir(self.IMAGES_DIR)
        for file_name in file_names:
            if os.path.exists(self.IMAGES_DIR + "/" + file_name):
                os.remove(self.IMAGES_DIR + "/" + file_name)

        # 2. 视频拆成图片，保存到临时文件夹
        video_processor = VideoProcessor()
        video_processor.video2images(video_path, self.IMAGES_DIR, freq=2)

        # 3. 多张图片，拼成gif
        start = time.clock()
        image_list = []
        file_names = os.listdir(self.IMAGES_DIR)

        file_names.sort(key=functools.cmp_to_key(self.file_cmp))
        for file_name in file_names:
            image_list.append(self.IMAGES_DIR + "/" + file_name)
        self.images2gif(image_list, gif_path, duration=0.1)

    def images2gif(self, image_path_list, gif_path, duration=0.2):
        """
        给定若干图片路径列表(已排好序的)，加载图片并拼接得到gif，图片将生成在与gif相同的路径下
        :param image_path_list: 若干图片路径
        :param gif_path: 生成的gif图片路径(带图片名称)
        :param duration: 生成的gif动图每张图片的时间间隔
        :return:
        """
        frames = []  # 读入缓冲区
        for image_path in image_path_list:
            frames.append(imageio.imread(image_path))
        imageio.mimsave(gif_path, frames, 'GIF', duration=duration)
        print("处理完成")

    def file_cmp(self, file_name1, file_name2):
        return int(file_name1.split('.')[0]) - int(file_name2.split('.')[0])


