from django.shortcuts import render
from django.http import HttpResponse

def front(request):
    return render(request, "questions/front.html")

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "questions/index.html")

def result_a(request):
    return render(request, "questions/result_a.html")

def result_b(request):
    return render(request, "questions/result_b.html")

def result_c(request):
    return render(request, "questions/result_c.html")
