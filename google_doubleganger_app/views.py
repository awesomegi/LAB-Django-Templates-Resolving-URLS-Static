# google_doubleganger_app/views.py

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'google_doubleganger_app/home_page.html')


def terms_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'google_doubleganger_app/terms_page.html')