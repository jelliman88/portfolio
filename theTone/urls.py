from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # homePage
    url('', include('homePage.urls', namespace='homePage')),
    # leBeau
    url('leBeau', include('leBeau.urls', namespace='leBeau')),
    # sportsApp
    url('sportsApp', include('sportsApp.urls', namespace='sportsApp')),
    # portfolio
    url('portfolio', include('portfolio.urls', namespace='portfolio')),
] 

urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)