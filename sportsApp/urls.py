from django.urls import path
from . import views


app_name = 'sportsApp'
urlpatterns = [
    path('', views.sportsApp, name='sportsApp'),
    path('<int:team_id>', views.teamDetail, name='teamDetail'),  
   
    
] 
