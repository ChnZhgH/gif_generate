"""gif_generate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gif_gen import views
from gif_gen.src.controller import gif_controller

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.index),
    path(r'upload_images', gif_controller.upload_images),
    path(r'upload/video', gif_controller.upload_video),
    path(r'transform', gif_controller.video_to_gif_quick),
    path(r'download/gif', gif_controller.download)

]
