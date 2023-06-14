from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProcessView.as_view(), name="questions"),
    path("result/", views.ResultView.as_view(), name="result"),
]