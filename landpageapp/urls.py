
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from landpageapp import views
from django.db import router

urlpatterns =([
   
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('team/', views.team, name='team'),
    # path('subscribe/', views.subscribe, name='subscribe'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    

