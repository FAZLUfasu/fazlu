from django.conf import settings
from django.urls import path
from . import views  # Make sure you're importing views
from django.conf.urls.static import static



app_name = 'unixapp'

urlpatterns =([
    
    path('', views.flutter_app, name='flutter_app'), 
 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
