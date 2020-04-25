from django.shortcuts import render
from django.http import JsonResponse
import os


# Create your views here.
def upload_video(request):
    if request.method == "POST":
        my_file = request.FILES.get("my_file", None)
        if not my_file:
            return JsonResponse({'message': 'no files to upload.'})
        destination = open(os.path.join(os.getcwd(), "tmp/videos", my_file.name), "wb+")
        for chunk in my_file.chunks():
            destination.write(chunk)
        destination.close()
        return JsonResponse({'message': 'upload over.'})


def upload_images(request):
    pass


def video_to_gif(request):
    pass


def images_to_gif(request):
    pass


if __name__ == '__main__':
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))
    a = os.path.join(PROJECT_ROOT, "tmp", "my_file.name")
    print(PROJECT_ROOT)
    print(a)
