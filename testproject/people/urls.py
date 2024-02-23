from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addperson", views.add_person, name="add_person"),
]