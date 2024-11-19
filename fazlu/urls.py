from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', include('landpageapp.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('cadmin/', include('cadmin.urls')),
    path('admin/', admin.site.urls), 
    path('app/', include('fasu.urls')), 
    
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)

