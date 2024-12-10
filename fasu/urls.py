from django.db import router
from fasu import views
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'team_photos', views.TeamMemberViewSet)


urlpatterns =([
    path('get_notifications/',views.get_notifications,name='get_notifications'),
    path('notifications/', views.NotificationListView.as_view(), name='notification_list'),
    path('Whatsappchat/', views.WhatsappchatView.as_view(), name='Whatsappchat'),
    path('news/', views.NewsUpdateListCreateView.as_view(), name='news-list-create'),
    path('summary/', views.SummaryAPIView.as_view(), name='summary'),
    path('gallery/', views.gallery_data, name='gallery_data'),
    path('videos/',views.VideouploadView.as_view(), name='video-upload'),
    path('upvideos/',views.VideoListView.as_view(), name='videos'),
    path('images/',views. ImageUploadView.as_view(),name='image-upload'),
    path('up/', views.ImageListView.as_view(), name='images'),
    path('team_photos/', include(router.urls)),
    path('loginn/',views.LoginView.as_view()),
    path('investorprofilecreate/', views.create_investor_profile, name='investorprofilecreate'),
    path('investorprofile/', views.InvestorProfileAPIView.as_view(), name='investorprofile'),
    path('HomePageData/', views.HomePageDataAPIView.as_view(), name='HomePageData'), 
    path('myprojects/', views.MyProjectsAPIView.as_view(), name='myproject-list-create'),
    path('Projectpage/', views.ProjectpageListAPIView.as_view(), name='Projectpage'), 
    path('join-table/', views.join_table_list, name='join-table-list'),
    path('teammember/',views.TeamMemberListAPIView.as_view(), name='teammember'),
    path('contactinfo/', views.ContactInfoAPIView.as_view(), name='contact_info'),
    path('AboutUs/', views.AboutUsPageAPIView.as_view(), name='AboutUs'),
    path('investorprofile/username/<str:username>/', views.profile_view),
    path('myprojects/username/<str:username>/', views. my_projects_view),
    path('forgot-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('register/', views.register, name='register'),
    path('get_video_notifications/', views.get_video, name='video_notifications'),
    path('videonotifications/', views.NotificationListView.as_view(), name='notification_list'),
    path('create-join-request/', views.create_join_request, name='create_join_request'),
    path('user-details/', views.UserDetailView.as_view(), name='user-details'),
     
   

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
