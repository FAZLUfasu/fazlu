from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = ([
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin', admin.site.urls),
    path('app/', include('fasu.urls')), 
    
   
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
)
