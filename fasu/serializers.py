from tkinter import Image

from django.conf import settings
from requests import Response
from .models import  AboutUs, BackgroundImage, ContactInfo, Dividend, Images, Join, Location, MyProjects, NewsUpdate, Notification, Projectpage, TeamMember, VideoNotification, Whatsappchat, video,Summary
from rest_framework import serializers
from .models import HomePageData, Login,InvestorProfile
from rest_framework import serializers,viewsets
from rest_framework.decorators import action
from django.contrib.auth.models import User

class WhatsappchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whatsappchat
        fields = ['phone_number', 'message']

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class NewsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsUpdate
        fields = ['id', 'title', 'description', 'date_published']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ['id', 'video', 'videoname', 'date_of_upload']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__' # Fields to include in the serializer
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class InvestorsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields = '__all__'
        
    def update(self, instance, validated_data):
        # Handle file uploads
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UpdateInvestorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields = '__all__'  # Include all fields in the model for updating
        extra_kwargs = {
            'email': {'read_only': True},  # Email is the primary key; make it read-only
        }

class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class VideoNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNotification
        fields = '__all__'
        

class MyProjectsSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = MyProjects
        fields = '__all__'

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Include other fields as needed


class ProjectpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectpage
        fields = '__all__'



class HomePageDataSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = HomePageData
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = [
            'name', 
            'role', 
            'photo', 
            'photo_url', 
            'facebook_url', 
            'twitter_url', 
            'linkedin_url', 
            'instagram_url', 
            'youtube_url'
        ]

    def get_photo_url(self, obj):
        # Construct the URL of the uploaded image
        if obj.photo:
            return obj.photo.url
        return None



class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'
       




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user

class UserRegisterView(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=201)
        return Response(serializer.errors, status=400)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = '__all__'  
class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class BackgroundImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackgroundImage
        fields = ['id', 'name', 'image']
    def get_image_url(self, obj):
        # Ensure the image URL is prefixed with MEDIA_URL
        return settings.MEDIA_URL + str(obj.image)
    


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'  # Include all fields from the Location model




class DividendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dividend
        fields = ['id', 'project', 'user', 'dividend_date', 'dividend_amount', 'transfer_proof']

    def create(self, validated_data):
        # Optionally handle any additional logic before saving the dividend
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Optionally handle updates
        return super().update(instance, validated_data)
