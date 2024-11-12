from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

<<<<<<< HEAD

urlpatterns = [
    path('', include('landpageapp.urls')),
    # Grappelli and admin URLs
    path('grappelli/', include('grappelli.urls')),  # Grappelli URLs
    path('admin/', admin.site.urls),  # Admin page UR0
    # Including URLs for other apps (like your "fasu" app)
    path('app/', include('fasu.urls')),  # Your app's URLs (fasu)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
urlpatterns = ([
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin', admin.site.urls),
    path('app/', include('fasu.urls')),  
    path('', include('landpageapp.urls')), 
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)
>>>>>>> 834b48be413c4af8c1665e675b7668b8020b3871
