from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', include('landpageapp.urls')),
    path('grappelli/', include('grappelli.urls')),  # Grappelli URLs
    path('admin/', admin.site.urls), 
    path('app/', include('fasu.urls')),  # Your app's URLs (fasu)
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)
