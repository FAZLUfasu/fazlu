
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('team/', views.team, name='team'),
    # path('subscribe/', views.subscribe, name='subscribe'),
]
# if settings.DEBUG:  
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
