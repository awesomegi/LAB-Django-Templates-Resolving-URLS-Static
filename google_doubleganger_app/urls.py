from django.urls import path, include
from . import views 

app_name = 'google_doubleganger_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('terms/', views.terms_view, name='terms_view'),
]