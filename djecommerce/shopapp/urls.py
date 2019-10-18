from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^accounts/', include('allauth.urls')),
]
