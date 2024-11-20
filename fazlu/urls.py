from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = ([
    path('', include('landpageapp.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('cadmin/', include('cadmin.urls')),
    path('admin/', admin.site.urls), 
<<<<<<< HEAD
    path('app/', include('fasu.urls')), 
    
=======
    path('cadmin/', include('cadmin.urls')),
    path('app/',include('fasu.url')), # Your app's URLs (fasu)
>>>>>>> 66c0aeeefa5da1a2ab751e927eacdc63d97422aa
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)

