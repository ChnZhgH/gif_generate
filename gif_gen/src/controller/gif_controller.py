from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def upload_video(request):
    pass


def upload_images(request):
    return JsonResponse({'status': 200, 'message': '添加成功'})


def mp4_to_gif(request):
    pass


def images_to_gif(request):
    pass
