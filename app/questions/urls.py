from django.urls import path
from . import views
from questions.views import ProcessView

app_name = "questions"
urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.page, name="page"),
    path('form', ProcessView.as_view(), name="Process"),
    path("test/result_a/", ProcessView.as_view(), name="Process"),
    path("test/result_b/", ProcessView.as_view(), name="Process"),
    path("test/result_c/", ProcessView.as_view(), name="Process")
]
