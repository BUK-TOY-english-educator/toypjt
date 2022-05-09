from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe


def index(request):
    return render(request, 'lectures/index.html')


def loading(request):
    return render(request, 'lectures/loading.html')


def study(request):
    pass


def writing(request):
    pass


def speaking(request, video_pk):
    return render(request, 'lectures/speaking.html')


def dashboard(request):
    pass


def save(request):
    pass

