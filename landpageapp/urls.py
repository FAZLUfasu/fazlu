
<<<<<<< HEAD
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from landpageapp import views
from django.db import router

urlpatterns =([
   
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
=======
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
>>>>>>> ca87fcd3052e845678370e87f4e4e2f577cb6287
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('team/', views.team, name='team'),
    # path('subscribe/', views.subscribe, name='subscribe'),
<<<<<<< HEAD
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    

=======
]
# if settings.DEBUG:  
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    #  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> ca87fcd3052e845678370e87f4e4e2f577cb6287
