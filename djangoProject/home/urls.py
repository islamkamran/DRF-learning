from django.urls import path
from .views import hello, post_todo

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('post-todo/', post_todo, name='post-todo')
]
