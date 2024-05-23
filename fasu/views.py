from django.http import JsonResponse
from django.shortcuts import render
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
from .forms import ImageUploadForm
from .serializers import JoinRequestSerializer,ProjectpageSerializer
from .serializers import AboutUsPageSerializer, ContactInfoSerializer, InvestorsProfileSerializer, MyProjectSerializer
from .serializers import RevenueSerializer, ExpenseSerializer,HomePageDataSerializer
from .serializers import NewProjectSerializer, OtherProjectSerializer, TeamMemberSerializer, VideoSerializer
from .models import Revenue, Expense,HomePageData,AboutUsPage
from .models import JoinRequest,Projectpage
from .models import ContactInfo, InvestorProfile, TeamMember, video
from .models import Image
from .models import MyProject






# class InvestorProfileAPIView(generics.ListCreateAPIView):
#     queryset = InvestorProfile.objects.all()
#     serializer_class = InvestorsProfileSerializer
   
#     @api_view(['GET'])
#     @permission_classes([IsAuthenticated])
#     def view_investor_profile(request):
#         try:
#             user_id = request.user.id  # Get user ID dynamically
#             investor_profile = InvestorProfile.objects.get(user_id=user_id)
#             serializer = InvestorsProfileSerializer(investor_profile)
#             return Response({"profile": serializer.data}, status=200)
#         except InvestorProfile.DoesNotExist:
#             return Response({"error": "Investor profile does not exist for this user"}, status=404)
#         except Exception as e:
#             return Response({"error": str(e)}, status=500)

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


class MyProjectAPIView(generics.ListCreateAPIView):
    queryset = MyProject.objects.all()
    serializer_class = MyProjectSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_myproject(request):
    try:
        user = request.user
        project = MyProject.objects.filter(user=user)
        serializer = MyProjectSerializer(project, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except MyProject.DoesNotExist:
        return Response({"error": "Project does not exist for this user"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_myproject(request):
    try:
        user = request.user
        serializer = MyProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response({"success": "Project created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class ImageView(APIView):
    def post(self, request, format=None):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            return Response({'image_url': image_instance.image.url}, status=status.HTTP_201_CREATED)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



def get_images(request):
    images = Image.objects.all()
    image_urls = [image.image.url for image in images]
    return JsonResponse({'image_urls': image_urls})




def my_view(request):
    instance = HomePageData.objects.get(pk=1)  # Retrieve a model instance
    image_url = instance.banner_image.url  # Access the URL of the image field
    # Other code...
    return render(request, 'my_template.html', {'instance': instance, 'image_url': image_url})






class InvestorProfileAPIView(generics.ListCreateAPIView):
    queryset = InvestorProfile.objects.all()
    serializer_class = InvestorsProfileSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        try:
            profile = InvestorProfile.objects.get(user=user)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        except InvestorProfile.DoesNotExist:
            return Response({"error": "Investor profile does not exist for this user"}, status=404)



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
           

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = video.objects.all()
    serializer_class = VideoSerializer

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
            about_us = AboutUsPage.objects.first()
            serializer = AboutUsPageSerializer(about_us)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AboutUsPage.DoesNotExist:
            return Response({'error': 'About us page not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class NewProject(APIView):
    def get(self, request, format=None):
        try:
            new_projects = NewProject.objects.all()
            serializer = NewProjectSerializer(new_projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class MyProject(APIView):
#     def get(self, request, format=None):
#         try:
#             my_projects = MyProject.objects.all()
#             serializer = MyProjectSerializer(my_projects, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class OtherProject(APIView):
    def get(self, request, format=None):
        try:
            other_projects = OtherProject.objects.all()
            serializer = OtherProjectSerializer(other_projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class RevenueListCreateAPIView(APIView):
    def get(self, request):
        revenues = Revenue.objects.all()
        serializer = RevenueSerializer(revenues, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RevenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseListCreateAPIView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class JoinRequestListCreateAPIView(APIView):
    def get(self, request):
        try:
            join_requests = JoinRequest.objects.all()
            serializer = JoinRequestSerializer(join_requests, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = JoinRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ProjectpageListAPIView(APIView):
    def get(self, request):
        try:
            projectpage = Projectpage.objects.all()
            serializer = ProjectpageSerializer(projectpage, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer