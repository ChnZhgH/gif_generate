import os

from gif_gen.src.service.gif_generator import GifGenerator


if __name__ == '__main__':
    VIDEOS_DIR = os.path.join(os.getcwd(), "tmp/videos")
    GIFS_DIR = os.path.join(os.getcwd(), "tmp/gifs")
    gif_gen = GifGenerator()
    gif_gen.video2gif(VIDEOS_DIR + "/屏幕录制2020-04-25上午12.35.53.mov", GIFS_DIR + "/屏幕录制2020-04-25上午12.35.53.gif")






