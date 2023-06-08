from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.page, name="page"),
    path('form',views.process_POST_request, name="process_POST_request"),
    path("test/result_a/", views.process_POST_request, name="result_a"),
    path("test/result_b/", views.process_POST_request, name="result_b"),
    path("test/result_c/", views.process_POST_request, name="result_c")
]