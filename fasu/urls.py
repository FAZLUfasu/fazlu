from django.db import router
from fasu import views
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'team_photos', views.TeamMemberViewSet)


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name='support'),
    path('team/', views.team, name='team'),
    path('app/get_notifications/',views.get_notifications,name='get_notifications'),
    path('app/notifications/', views.NotificationListView.as_view(), name='notification_list'),
    path('app/Whatsappchat/', views.WhatsappchatView.as_view(), name='Whatsappchat'),
    path('app/news/', views.NewsUpdateListCreateView.as_view(), name='news-list-create'),
    path('app/summary/', views.SummaryAPIView.as_view(), name='summary'),
    path('app/gallery/', views.gallery_data, name='gallery_data'),
    path('app/videos/',views.VideoListCreateView.as_view(), name='video-list-create'),
    path('app/images/',views. ImageUploadView.as_view(),name='images'),
    path('app/up/', views.ImageListView.as_view(), name='image-upload'),
    path('app/team_photos/', include(router.urls)),
    path('app/loginn/',views.LoginView.as_view()),
    path('app/investorprofilecreate/', views.create_investor_profile, name='investorprofilecreate'),
    path('app/investorprofile/', views.InvestorProfileAPIView.as_view(), name='investorprofile'),
    path('app/HomePageData/', views.HomePageDataAPIView.as_view(), name='HomePageData'), 
    path('app/myprojects/', views.MyProjectsAPIView.as_view(), name='myproject-list-create'),
    path('app/Projectpage/', views.ProjectpageListAPIView.as_view(), name='Projectpage'), 
    path('app/join-table/', views.join_table_list, name='join-table-list'),
    path('app/teammember/',views.TeamMemberListAPIView.as_view(), name='teammember'),
    path('app/contactinfo/', views.ContactInfoAPIView.as_view(), name='contact_info'),
    path('app/AboutUs/', views.AboutUsPageAPIView.as_view(), name='AboutUs'),
    path('app/investorprofile/username/<str:username>/', views.profile_view),
    path('app/myprojects/username/<str:username>/', views. my_projects_view),
    path('app/create-join-request/', views.create_join_request, name='create_join_request'),
    path('app/user-details/', views.UserDetailView.as_view(), name='user-details'),
    ]
if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)