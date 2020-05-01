from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('amz_sfr_tracker/', include('amz_sfr_tracker.urls')),
    path('accounts/', include('accounts.urls')),
    path('amz_brands/', include('amz_brands.urls')),
    path('admin/', admin.site.urls),
]
