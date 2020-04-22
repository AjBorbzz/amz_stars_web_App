from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='brands'),
    path('<int:brand_id>', views.brand_details, name='brand_details'),
]
