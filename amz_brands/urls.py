from django.urls import path

from . import views

urlpatterns = [

    path('<int:brand_id>', views.brand_details, name='brand_details'),
]
