import os
import moviepy.editor as mpy


class GifGenerator(object):
    def __init__(self):
        self.IMAGES_DIR = os.path.join(os.getcwd(), "tmp/images")

    def video2gif_quick(self, video_path, gif_path):
        content = mpy.VideoFileClip(video_path)
        content.write_gif(gif_path, fps=5)



