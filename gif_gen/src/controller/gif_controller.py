import json
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
import os


# Create your views here.
from gif_gen.src.service.gif_generator import GifGenerator
from gif_gen.src.utils import build_gif_name


def upload_video(request):
    if request.method == "POST":
        my_file = request.FILES.get("my_file", None)
        if not my_file:
            return JsonResponse({'message': 'no files to upload.'})
        file_path = os.path.join(os.getcwd(), "tmp/videos", my_file.name)
        destination = open(file_path, "wb+")
        for chunk in my_file.chunks():
            destination.write(chunk)
        destination.close()
        return JsonResponse({'file_path': file_path, 'file_name': my_file.name})


def upload_images(request):
    pass


def video_to_gif(request):
    GIFS_DIR = os.path.join(os.getcwd(), "tmp/gifs/")
    gif_gen = GifGenerator()
    # video_path = eval(request.body.decode()).get('video_path')
    body = json.loads(request.body.decode())
    video_path = body.get('video_path')
    video_name = body.get('video_name')
    gif_name = build_gif_name(video_name)

    gif_gen.video2gif(video_path, GIFS_DIR + gif_name)
    return JsonResponse({'message': 'transform over.'})


def images_to_gif(request):
    pass


def download(request):
    GIFS_DIR = os.path.join(os.getcwd(), "tmp/gifs/")
    video_name = request.GET.get('video_name')
    gif_name = build_gif_name(video_name)
    file = open(GIFS_DIR + gif_name, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/form-data'
    # content_dis = 'attachment;filename="' + gif_name + '"'
    # response['Content-Disposition'] = content_dis
    return response


if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
    a = os.path.join(PROJECT_ROOT, "tmp", "my_file.name")
    print(PROJECT_ROOT)
    print(a)
