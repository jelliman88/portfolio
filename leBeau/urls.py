from django.urls import path
from . import views

app_name = 'leBeau'
urlpatterns = [
    path('/<str:urlTag>/<str:order>/<str:status>/', views.leBeau, name='leBeau'), 
    path('edit/<int:id>', views.leBeauEdit, name='leBeauEdit'), 
    path(r'^tags', views.tagSearch, name='tagSearch'), 
    
]