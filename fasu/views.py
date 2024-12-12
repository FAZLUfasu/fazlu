
import json
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render, redirect
from .serializers import  BackgroundImageSerializer, UserSerializer, VideoNotificationSerializer
from django.contrib.auth.views import PasswordResetView
from .serializers import AboutUsPageSerializer, ImagesSerializer, JoinSerializer, MyImageSerializer, MyProjectsSerializer, NewsUpdateSerializer, NotificationSerializer,ProjectpageSerializer, SummarySerializer, UserSerializer, WhatsappchatSerializer
from .serializers import  ContactInfoSerializer, InvestorsProfileSerializer
from .serializers import HomePageDataSerializer
from .serializers import  TeamMemberSerializer, VideoSerializer
from .models import  AboutUs, Backgroundimage,  MyProjects, NewsUpdate, HomePageData, Notification, Summary, Whatsappchat
from .models import Join,Projectpage
from .models import ContactInfo, InvestorProfile, TeamMember, video
from .models import Images,video
# from .models import MyProject
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User



from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        # Customize the response as needed
        return Response({'token': token.key})



# Generate token for authenticated user
def generate_token(user):
    token = AccessToken.for_user(user)
    return str(token)




def join_table_list(request):
    # Query the join table to retrieve all entries
    join_table_entries = Join.objects.all()

    # Serialize the data
    serializer = JoinSerializer(join_table_entries, many=True)

    # Return the serialized data as a JSON response
    return JsonResponse(serializer.data, safe=False)
class WhatsappchatView(generics.RetrieveAPIView):
    queryset = Whatsappchat.objects.all()
    serializer_class = WhatsappchatSerializer

    def get_object(self):
        return Whatsappchat.objects.first()


class MyProjectsAPIView(generics.ListCreateAPIView):
    queryset = MyProjects.objects.all()
    serializer_class = MyProjectsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_myprojects(request):
    try:
        user = request.user
        project = MyProjects.objects.filter(user=user)
        serializer = MyProjectsSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except MyProjects.DoesNotExist:
        return Response({"error": "Project does not exist for this user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_myprojects(request):
    try:
        user = request.user
        serializer = MyProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"success": "Project created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SummaryAPIView(generics.ListCreateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class NewsUpdateListCreateView(generics.ListCreateAPIView):
    queryset = NewsUpdate.objects.all().order_by('-date_published')
    serializer_class = NewsUpdateSerializer

    


class VideouploadView(APIView):
     parser_classes = (MultiPartParser, FormParser)

     def post(self, request, *args, **kwargs):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            video_instance = serializer.save()
            # Create or update the notification
            videonotification, created = Notification.objects.get_or_create(
                defaults={'message': 'New video uploaded!'},
                last_uploaded_video_id=video_instance.id
            )
            if not created:
                videonotification.last_uploaded_image_id = video_instance.id
                videonotification.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ImagesSerializer(data=request.data)
        if serializer.is_valid():
            image_instance = serializer.save()
            # Create or update the notification
            notification, created = Notification.objects.get_or_create(
                defaults={'message': 'New image uploaded!'},
                last_uploaded_image_id=image_instance.id
            )
            if not created:
                notification.last_uploaded_image_id = image_instance.id
                notification.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NotificationListView(APIView):
    def get(self, request, format=None):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
def get_notifications(request):
    notifications = Notification.objects.all()
    data = {
    'notifications': list(notifications.values())
    }
    return JsonResponse(data)

class VideoNotificationListView(APIView):
    def get(self, request, format=None):
        videonotifications = Notification.objects.all()
        serializer = VideoNotificationSerializer(videonotifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def get_video(request):
    videonotifications = video.objects.all()
    data = {
    'videonotifications': list(videonotifications.values())
    }
    return JsonResponse(data)


def my_projects_view(request, username):
    try:
        # Retrieve the user based on the provided username
        user = User.objects.get(username=username)
        
        # Fetch projects associated with the user
        projects = MyProjects.objects.filter(user=user)
        
        # Serialize the projects data
        serialized_projects = MyProjectsSerializer(projects, many=True)
        
        return JsonResponse(serialized_projects.data, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def profile_view(request, username):
    try:
        user = User.objects.get(username=username)
        profile = InvestorProfile.objects.get(user=user)
        
        # Serialize the profile data as needed
        profile_data = {
            'username': profile.user.username,
            'email': profile.user.email,
            # Add other profile fields as needed...
        }
        
        # Add all profile fields to profile_data
        profile_data.update(profile.__dict__)
        
        # Remove unnecessary fields
        profile_data.pop('_state', None)  # Remove _state field
        
        return JsonResponse(profile_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except InvestorProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)






class InvestorProfileAPIView(generics.ListCreateAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorsProfileSerializer
   
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def view_investor_profile(request):
        try:

            user = request.user
            profile = [InvestorProfile.objects.get(user=user)]
            serializer = InvestorsProfileSerializer(profile)

        # You may customize the response data based on your requirements
            return Response({"profile": profile.serialize()}, status=200)
        except InvestorProfile.DoesNotExist:
            return Response({"error": "Investor profile does not exist for this user"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_investor_profile(request):
    try:
        user = request.user
        if InvestorProfile.objects.filter(user=user).exists():
            return Response({"error": "Investor profile already exists for this user"}, status=400)
        profile = InvestorProfile(user=user)
        profile.save()
        return Response({"success": "Investor profile created successfully"}, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(InvestorProfile, user=user)
        serializer = InvestorsProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LoginView(APIView):

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)  # Corrected assignment

            return Response({'token': token.key}, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
           


class VideoListView(generics.ListAPIView):
    queryset = video.objects.all()
    serializer_class = VideoSerializer

class ImageListView(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

class HomePageDataAPIView(APIView):
    def get(self, request):
        try:
            homepage_data = HomePageData.objects.all()
            serializer = HomePageDataSerializer(homepage_data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberListAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            team_members = TeamMember.objects.all()
            serializer = TeamMemberSerializer(team_members, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TeamMember.DoesNotExist:
            return Response({'error': 'Team members not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ContactInfoAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            about_us = ContactInfo.objects.first()
            serializer = ContactInfoSerializer(about_us)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ContactInfo.DoesNotExist:
            return Response({'error': 'ContactInfo not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AboutUsPageAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        try:
            about_us = AboutUs.objects.first()
            serializer = AboutUsPageSerializer(about_us)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AboutUs.DoesNotExist:
            return Response({'error': 'About us page not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class VideoNotificationListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        videonotifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
        serializer = VideoNotificationSerializer(videonotifications, many=True)
        return Response(serializer.data)


class ProjectpageListAPIView(APIView):
    def get(self, request):
        try:
            projectpage = Projectpage.objects.all()
            serializer = ProjectpageSerializer(projectpage, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)







def gallery_data(request):
    # Retrieve all images and videos from the database
    images = Images.objects.all()
    videos = video.objects.all()

    # Extract URLs from images and videos
    image_urls = [image.image.url for image in images]
    video_urls = [video.video.url for video in videos]

    # Return the URLs as JSON response
    return JsonResponse({'images': image_urls, 'videos': video_urls})




@api_view(['POST'])
def create_join_request(request):
    serializer = JoinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)





def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html') 

def privacy(request):
    return render(request, 'privacy.html') 

def support(request):
    return render(request, 'support.html') 

def team(request):
    return render(request, 'team.html') 





def about_view(request):
    url = "https://unix-aquatics.com/app/AboutUs/"
    response = request.get(url)
    about_data = response.json() if response.status_code == 200 else {}

    return render(request, 'about.html', {'about_data': about_data})


def team_page(request):
    response = request.get("https://unix-aquatics.com/app/teammember/")
    team_members = response.json()  # Assuming the API returns the team data in JSON format

    return render(request, 'team.html', {'team_members': team_members})



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if username and email and password:
            user = User.objects.create_user(username=username, email=email, password=password)
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)



import json
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def reset_password(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             email = data.get('email')

#             if not email:
#                 return JsonResponse({'error': 'Email is required'}, status=400)

#             user = User.objects.filter(email=email).first()

#             if not user:
#                 return JsonResponse({'error': 'User with this email does not exist'}, status=404)

#             # Generate the reset token and user ID
#             uid = urlsafe_base64_encode(str(user.pk).encode())
#             token = default_token_generator.make_token(user)

#             # Generate reset URL (e.g., frontend URL)
#             reset_url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"

#             # Build the email content
#             subject = "Reset Your Password"
#             message = render_to_string('password_reset_email.html', {'reset_url': reset_url})

#             # Send email
#             send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

#             return JsonResponse({'message': 'Password reset email sent!'}, status=200)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class ResetPasswordView(APIView):
    @csrf_exempt
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # Generate token and uid
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Build the reset link
        reset_url = f"https://unix-aquatics.com/reset/{uid}/{token}/"

        # Render email template
        subject = "Reset Your Password"
        message = render_to_string('registration/password_reset_email.html', {
            'user': user,
            'reset_url': reset_url,
        })

        try:
            # Send the email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset email sent!'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': f'Failed to send email: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@csrf_exempt
def reset_password_confirm(request, uidb64, token):
    try:
        # Decode the UID from the URL
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Password has been reset successfully.'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid form data.'}, status=400)
        else:
            form = SetPasswordForm(user)
        return render(request, 'registration/password_reset_confirm.html', {'form': form})

    else:
        return JsonResponse({'error': 'Invalid reset token'}, status=400)

 
 





class BackgroundImageView(APIView):
    def get(self, request):
        """
        Return all background images.
        """
        bg_images = Backgroundimage.objects.all()
        serializer = BackgroundImageSerializer(bg_images, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Upload a new background image.
        """
        serializer = BackgroundImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)