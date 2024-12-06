from tkinter import Image
from .models import  AboutUs, ContactInfo, Images, Join, MyProjects, NewsUpdate, Notification, Projectpage, TeamMember, Whatsappchat, video,Summary
from rest_framework import serializers
from .models import HomePageData, Login,InvestorProfile
from rest_framework import serializers
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

class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
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