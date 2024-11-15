from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', include('landpageapp.urls')),
    path('grappelli/', include('grappelli.urls')),  # Grappelli URLs
    path('admin/', admin.site.urls),  # Admin URL
    path('app/', include('fasu.urls')),  # Your app's URLs (fasu)
=======
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = ([
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin', admin.site.urls),
    path('app/', include('fasu.urls')),  
    path('app/', include('landpageapp.urls')), 
>>>>>>> ca87fcd3052e845678370e87f4e4e2f577cb6287
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)
