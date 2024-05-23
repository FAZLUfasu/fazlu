from tkinter import Image
from .models import  ContactInfo, JoinRequest, Projectpage, TeamMember, video
from rest_framework import serializers
from .models import AboutUsPage, Expense, HomePageData, Login,InvestorProfile, MyProject, NewProject, OtherProject, Revenue
from rest_framework import serializers



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = video
        fields = ['id', 'video', 'videoname', 'date_of_upload']

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__' # Fields to include in the serializer


class InvestorsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestorProfile
        fields = '__all__'

class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class AboutUsPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsPage
        fields = '__all__'

        
class NewProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProject
        fields = '__all__'

        
class MyProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProject
        fields = '__all__'



class JoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = '__all__'



class ProjectpageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectpage
        fields = '__all__'




class OtherProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherProject
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
        fields = [ 'name', 'role', 'photo', 'photo_url']

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