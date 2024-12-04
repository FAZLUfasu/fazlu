from django.conf import settings
from django.urls import path
from . import views  # Make sure you're importing views
from django.conf.urls.static import static



app_name = 'cadmin'

urlpatterns = [
    path('investor-profiles/', views.investor_profiles_view, name='investor_profiles'),
    path('investor-profile/create/<str:email>/', views.create_investor_profile, name='create_investor_profile'),
    path('investor-profile/update/<int:pk>/', views.update_investor_profile, name='update_investor_profile'),
    path('investor-profile/delete/<int:pk>/', views.delete_investor_profile, name='delete_investor_profile'),





    path('my-project/', views.my_project_page_view, name='my_project_page'),
    path('project/', views.project_page_view, name='project_page'),
    path('team/', views.team_members_view, name='team_members'),
    path('index/', views.index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
