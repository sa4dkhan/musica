from django.urls import path
from music import views

app_name = 'music'
urlpatterns = [
    path('create_album', views.create_album, name='create_album')
]