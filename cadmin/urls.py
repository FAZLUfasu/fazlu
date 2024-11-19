from django.conf import settings
from django.urls import path
from . import views  # Make sure you're importing views
from django.conf.urls.static import static

urlpatterns = [
    path('investor-profiles/', views.investor_profiles_view, name='investor_profiles'),
    path('my-project/', views.my_project_page_view, name='my_project_page'),
    path('project/', views.project_page_view, name='project_page'),
    path('team/', views.team_members_view, name='team_members'),
    path('index/', views.index, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
