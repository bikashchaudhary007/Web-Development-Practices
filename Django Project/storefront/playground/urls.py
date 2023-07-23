from django.urls import path
from .import views

#URLCongif
urlpatterns = [
    path('hello/', views.say_hello)
]