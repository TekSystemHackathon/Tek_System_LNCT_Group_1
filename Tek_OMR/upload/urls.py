from django.urls import path
from .views import simple_upload, home

urlpatterns = [
    path('upload/', simple_upload),
    path('', home, name='home'),
]
