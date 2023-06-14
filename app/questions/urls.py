from django.urls import path
from . import views
from questions.views import ProcessView, ResultView

app_name = "questions"
urlpatterns = [
    path("", ProcessView.as_view(), name='questions'),
    path('result/', ResultView.as_view(), name="result"),
]

