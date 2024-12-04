from django import forms
from fasu.models import InvestorProfile

class InvestorProfileForm(forms.ModelForm):
    class Meta:
        model = InvestorProfile
        fields = [
            'email',           # Include email field
            'name',
            'address',
            'mobile_number',
            'whatsapp',
            'profilepic',
            'aadhar_card',
            'aadhar_card_attachment',
            'election_id',
            'election_id_attachment',
            'passport_number',
            'passport_attachment',
            'pan_card_number',
            'pan_card_attachment',
            'account_number',
            'iban',
            'bank_name',
            'branch',
            'ifsc_code',
            'bank_account_passbook_attachment',
        ]

    def clean_email(self):
        email = self.cleaned_data['email']
        # Check if the email already exists in the database
        if InvestorProfile.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already associated with an investor profile.")
        return email
