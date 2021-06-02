from django.urls import path
from . import views

app_name = 'homePage'
urlpatterns = [
    path('', views.homePage, name='homePage'), 
    path('contact', views.contact, name='contact'),
    
    
]