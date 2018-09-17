from django.urls import path
from music import views

app_name = 'music'
urlpatterns = [
    #REGISTER
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('create_album', views.create_album, name='create_album'),
    path

]