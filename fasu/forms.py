# forms.py

from django import forms
from .models import Images, InvestorProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = [
            'profilepic', 'aadhar_card_attachment', 'election_id_attachment', 
            'passport_attachment', 'pan_card_attachment', 'bank_account_passbook_attachment'
        ]
        widgets = {
            'profilepic': forms.ClearableFileInput(attrs={'multiple': False}),
            'aadhar_card_attachment': forms.ClearableFileInput(attrs={'multiple': False}),
            'election_id_attachment': forms.ClearableFileInput(attrs={'multiple': False}),
            'passport_attachment': forms.ClearableFileInput(attrs={'multiple': False}),
            'pan_card_attachment': forms.ClearableFileInput(attrs={'multiple': False}),
            'bank_account_passbook_attachment': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    # Override the clean method to handle multiple file fields properly
    def clean_profilepic(self):
        files = self.cleaned_data.get('profilepic')
        if isinstance(files, list):
            return files
        return [files]  # Return as a list even if it's a single file

    # You can apply the same clean method to other fields if needed
