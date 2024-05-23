from django.db import router
from fasu import views
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
router.register(r'team_photos', views.TeamMemberViewSet)

urlpatterns = [
    
    # path('upload/', views.upload_image, name='upload_image'),
    path('videos/',views.VideoListCreateView.as_view(), name='video-list-create'),
    path('images/',views.get_images, name='get_images'),
    path('up/', views.ImageView.as_view(), name='image-upload'),
    path('team_photos/', include(router.urls)),
    path('loginn/',views.LoginView.as_view()),
    path('investorprofilecreate/', views.create_investor_profile, name='investorprofilecreate'),
    path('investorprofile/', views.InvestorProfileAPIView.as_view(), name='investorprofile'),
    path('HomePageData/', views.HomePageDataAPIView.as_view(), name='HomePageData'), 
    path('NewProject/', views.NewProject.as_view(), name='NewProject'), 
    path('myprojects/', views.MyProjectAPIView.as_view(), name='myproject-list-create'),
    path('myproject/', views.view_myproject, name='view-myproject'),
    path('myproject/create/', views.create_myproject, name='create-myproject'),
    path('OtherProject/', views.OtherProject.as_view(), name='OtherProject'), 
    path('Revenue/', views.RevenueListCreateAPIView.as_view(), name='Revenue'), 
    path('Expense/', views.ExpenseListCreateAPIView.as_view(), name='Expense'),
    path('Projectpage/', views.ProjectpageListAPIView.as_view(), name='Projectpage'), 
    path('JoinRequest/', views.JoinRequestListCreateAPIView.as_view(), name='JoinRequest'),
    path('teammember/',views.TeamMemberListAPIView.as_view(), name='teammember'),
    path('contactinfo/', views.ContactInfoAPIView.as_view(), name='contact_info'),
    path('AboutUs/', views.AboutUsPageAPIView.as_view(), name='AboutUs'),
    path('investorpro/<int:id>/', views.InvestorProfileAPIView.as_view(), name='investor_profile_api'),
 
  
    ]
if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)