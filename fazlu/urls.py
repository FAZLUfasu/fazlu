from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from fazlu.fasu import views

urlpatterns = ([
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin', admin.site.urls),
    path('app/', include('fasu.urls')), 
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('team/', views.team, name='team'),
   
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)
