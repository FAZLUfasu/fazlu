# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_views

# urlpatterns = ([
#     path('', include('landpageapp.urls')),
#     path('grappelli/', include('grappelli.urls')),
#     path('admin/', admin.site.urls), 
#     path('cadmin/', include('cadmin.urls',namespace='cadmin')),
#     path('app/',include('fasu.urls')), 
#     path('unixapp/',include('unixapp.urls')),

#     path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
#     path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# )


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = ([
    path('', include('landpageapp.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('cadmin/', include('cadmin.urls', namespace='cadmin')),
    path('app/', include('fasu.urls')),
    path('unixapp/', include('unixapp.urls')),

    # Password reset views
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT))

