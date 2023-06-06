from django.urls import path

from . import views

urlpatterns = [
    path("", views.front, name="front"),
    path("test/", views.index, name="index"),
    path("result_a/", views.process_POST_request, name="result_a"),
    path("result_b/", views.process_POST_request, name="result_b"),
    path("result_c/", views.process_POST_request, name="result_c")
]