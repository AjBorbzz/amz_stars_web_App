from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('enroll', views.enroll, name='enroll'),
    path('upload_file', views.upload_file, name='upload_file'),
]
