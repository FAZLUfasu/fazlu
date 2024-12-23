
import json
from django.forms import model_to_dict
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
from .serializers import  BackgroundImageSerializer, DividendSerializer, LocationSerializer, UserSerializer, VideoNotificationSerializer
from django.contrib.auth.views import PasswordResetView
from .serializers import AboutUsPageSerializer, ImagesSerializer, JoinSerializer, MyImageSerializer, MyProjectsSerializer, NewsUpdateSerializer, NotificationSerializer,ProjectpageSerializer, SummarySerializer, UserSerializer, WhatsappchatSerializer
from .serializers import  ContactInfoSerializer, InvestorsProfileSerializer
from .serializers import HomePageDataSerializer
from .serializers import  TeamMemberSerializer, VideoSerializer
from .models import  AboutUs, BackgroundImage, Dividend, Location,  MyProjects, NewsUpdate, HomePageData, Notification, Summary, Whatsappchat
from .models import Join,Projectpage
from .models import ContactInfo, InvestorProfile, TeamMember, video
from .models import Images,video
# from .models import MyProject
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
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
from django.contrib.auth.forms import SetPasswordForm
# from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        # Customize the response as needed
        return Response({'token': token.key})



# # Generate token for authenticated user
# def generate_token(user):
#     token = AccessToken.for_user(user)
#     return str(token)




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
    notifications = Images.objects.all()
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



# def profile_view(request, username):
#     try:
#         user = User.objects.get(username=username)
#         profile = InvestorProfile.objects.get(user=user)
        
#         # Serialize the profile data as needed
#         profile_data = {
#             'username': profile.user.username,
#             'email': profile.user.email,
#             # Add other profile fields as needed...
#         }
        
#         # Add all profile fields to profile_data
#         profile_data.update(profile.__dict__)
        
#         # Remove unnecessary fields
#         profile_data.pop('_state', None)  # Remove _state field
        
#         return JsonResponse(profile_data)
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User not found'}, status=404)
#     except InvestorProfile.DoesNotExist:
#         return JsonResponse({'error': 'Profile not found'}, status=404)




def profile_view(request, username):
    try:
        # Get user and profile
        user = User.objects.get(username=username)
        profile = InvestorProfile.objects.get(user=user)
        
        # Serialize the profile data
        profile_data = model_to_dict(profile)
        
        # If you have image fields like profile_pic, add the URL instead of the file object
        if profile.profile_pic:
            profile_data['profile_pic'] = profile.profile_pic.url
        
        # Remove unnecessary fields like '_state'
        profile_data.pop('_state', None)
        
        return JsonResponse(profile_data)
    
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except InvestorProfile.DoesNotExist:
        return JsonResponse({'error': 'Profile not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


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



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_investor_profile(request, username):
    try:
        # Get the user's profile
        user = request.user
        profile = InvestorProfile.objects.get(user=user)
        
        # Handle non-attachment fields first
        profile.name = request.data.get('name', profile.name)
        profile.address = request.data.get('address', profile.address)
        profile.mobile_number = request.data.get('mobile_number', profile.mobile_number)
        profile.email = request.data.get('email', profile.email)
        profile.whatsapp = request.data.get('whatsapp', profile.whatsapp)
        profile.aadhar_card = request.data.get('aadhar_card', profile.aadhar_card)
        profile.election_id = request.data.get('election_id', profile.election_id)
        profile.passport_number = request.data.get('passport_number', profile.passport_number)
        profile.pan_card_number = request.data.get('pan_card_number', profile.pan_card_number)
        profile.account_number = request.data.get('account_number', profile.account_number)
        profile.iban = request.data.get('iban', profile.iban)
        profile.bank_name = request.data.get('bank_name', profile.bank_name)
        profile.branch = request.data.get('branch', profile.branch)
        profile.ifsc_code = request.data.get('ifsc_code', profile.ifsc_code)
        
        # Handle attachment fields (only update if a new file is provided)
        if 'profilepic' in request.FILES:
            profile.profilepic = request.FILES['profilepic']
        if 'aadhar_card_attachment' in request.FILES:
            profile.aadhar_card_attachment = request.FILES['aadhar_card_attachment']
        if 'election_id_attachment' in request.FILES:
            profile.election_id_attachment = request.FILES['election_id_attachment']
        if 'passport_attachment' in request.FILES:
            profile.passport_attachment = request.FILES['passport_attachment']
        if 'pan_card_attachment' in request.FILES:
            profile.pan_card_attachment = request.FILES['pan_card_attachment']
        if 'bank_account_passbook_attachment' in request.FILES:
            profile.bank_account_passbook_attachment = request.FILES['bank_account_passbook_attachment']
        
        profile.save()  # Save the updated profile
        return Response({"success": "Investor profile updated successfully"}, status=status.HTTP_200_OK)
    
    except InvestorProfile.DoesNotExist:
        return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_investor_profile(request):
    try:
        user = request.user
        if InvestorProfile.objects.filter(user=user).exists():
            return Response({"error": "Investor profile already exists for this user"}, status=400)

        # Create a profile instance and save the file fields
        profile_data = request.data
        profile_data['user'] = user.id  # Ensure the user is linked to the profile
        profile_serializer = InvestorsProfileSerializer(data=profile_data, context={'request': request})

        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response({"success": "Investor profile created successfully", "profile": profile_serializer.data}, status=201)
        return Response({"error": profile_serializer.errors}, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(InvestorProfile, user=user)
        serializer = InvestorsProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(InvestorProfile, user=user)
        profile_serializer = InvestorsProfileSerializer(profile, data=request.data, context={'request': request}, partial=True)
        
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_200_OK)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
           

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_investor_profile(request):
#     try:
#         user = request.user
#         if InvestorProfile.objects.filter(user=user).exists():
#             return Response({"error": "Investor profile already exists for this user"}, status=400)
#         profile = InvestorProfile(user=user)
#         profile.save()
#         return Response({"success": "Investor profile created successfully"}, status=201)
#     except Exception as e:
#         return Response({"error": str(e)}, status=500)


# class ProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, username):
#         user = get_object_or_404(User, username=username)
#         profile = get_object_or_404(InvestorProfile, user=user)
#         serializer = InvestorsProfileSerializer(profile)
#         return Response(serializer.data, status=status.HTTP_200_OK)


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



# @api_view(['POST'])
# def register(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         if username and email and password:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        # Retrieve the data from the request
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        
        # Ensure all required fields are present
        if username and email and password and first_name and last_name:
            # Create a new user with the provided information
            user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        else:
            # Return an error response if any required field is missing
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)









# class DeleteAccountView(APIView):
#     permission_classes = [IsAuthenticated]  # Only authenticated users can delete their accounts

#     def delete(self, request, *args, **kwargs):
#         user = request.user  # The current logged-in user

#         try:
#             # Delete the user
#             user.delete()

#             # Optionally: You can delete related data (posts, comments, etc.) here if needed
#             # Example: Post.objects.filter(user=user).delete()

#             return Response({"message": "Account successfully deleted."}, status=status.HTTP_204_NO_CONTENT)

#         except Exception as e:
#             return Response({"message": f"Error deleting account: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class DeleteAccountView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete their account

    def delete(self, request, *args, **kwargs):
        user = request.user  # Get the currently authenticated user

        try:
            # Delete the user account
            user.delete()

            # Optionally, you can delete associated data (e.g., user posts, comments, etc.)
            # Example: Post.objects.filter(user=user).delete()

            return Response({"message": "Account successfully deleted."}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as e:
            return Response({"message": f"Error deleting account: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









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

 
 


class BackgroundImageView(generics.ListAPIView):
    queryset = BackgroundImage.objects.all()
    serializer_class = BackgroundImageSerializer



class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer



from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def get_user_details(request):
    # Get username from query params
    username = request.GET.get('username', None)

    if username is None:
        return Response({"error": "Username not provided"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch user based on username
        user = User.objects.get(username=username)

        # Return user details (you can customize what data you want to send)
        user_data = {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "date_joined": user.date_joined,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
        }

        return Response(user_data, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    

    

from rest_framework.decorators import action

class DividendViewSet(viewsets.ModelViewSet):
    queryset = Dividend.objects.all()
    serializer_class = DividendSerializer

    # Optionally add actions such as a custom endpoint for specific functionality
    @action(detail=True, methods=['get'])
    def get_total_dividend(self, request, pk=None):
        # Get the total dividend for a project or user
        dividend = self.get_object()
        total_dividend = sum(d.dividend_amount for d in dividend.project.dividends.all())
        return Response({"total_dividend": total_dividend}, status=status.HTTP_200_OK)
    

