from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('enroll', views.enroll, name="enroll"),
    path('reports', views.reports, name="reports"),
    path('account_details', views.account_details, name="account_details")
]
