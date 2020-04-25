import cv2


class VideoProcessor(object):
    def __init__(self):
        print()

    def load_video(self, path):
        pass

    def video2images(self, video_path, save_path, freq=5):
        """
        读取视频并转换为图片，默认每秒5张
        :param video_path: 视频所在路径
        :param save_path: 图片保存的文件夹路径
        :param freq: 每秒取几张
        :return:
        """
        vc = cv2.VideoCapture(video_path)
        # 一帧一帧的分割 需要几帧写几
        c = 0
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False
        while rval:
            rval, frame = vc.read()
            # 每秒提取5帧图片
            if c % freq == 0:
                cv2.imwrite(save_path + "/" + str('%06d' % c) + '.jpg', frame)
                cv2.waitKey(1)
            c = c + 1






