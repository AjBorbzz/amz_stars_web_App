from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('amz_brands.urls')),
    path('admin/', admin.site.urls),
]
