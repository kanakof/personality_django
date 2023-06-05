from django.urls import path

from . import views

urlpatterns = [
    path("", views.front, name="front"),
    # path("", views.index, name="index")

]