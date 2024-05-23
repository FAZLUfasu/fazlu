from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



class Login(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    


class InvestorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    profilepic = models.ImageField(upload_to='profilpic_attachments/',blank=True,)
    profilepicname =models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(primary_key=True)  # Primary key
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    aadhar_card = models.CharField(max_length=12, blank=True, null=True)
    aadhar_card_attachment = models.FileField(upload_to='aadhar_card_attachments/', blank=True, null=True)
    election_id = models.CharField(max_length=20, blank=True, null=True)
    election_id_attachment = models.FileField(upload_to='election_id_attachments/', blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_attachment = models.FileField(upload_to='passport_attachments/', blank=True, null=True)
    pan_card_number = models.CharField(max_length=10, blank=True, null=True)
    pan_card_attachment = models.FileField(upload_to  ='pan_card_attachments/', blank=True, null=True)
    
    
    account_number = models.CharField(max_length=50,blank=True, null=True)
    iban = models.CharField(max_length=50,blank=True, null=True)
    bank_name = models.CharField(max_length=100,blank=True, null=True)
    branch = models.CharField(max_length=100,blank=True, null=True)
    ifsc_code = models.CharField(max_length=20,blank=True, null=True)
    bank_account_passbook_attachment = models.FileField(upload_to='bank_account_passbook_attachments/', blank=True, null=True)
    id= models.CharField(max_length=100,blank=True, null=True)
   
    def __str__(self):
        return self.name


class NewProject(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    date_of_establishment = models.DateField()
    number_of_ponds = models.PositiveIntegerField()
    water_capacity = models.FloatField()  # Assuming in liters or cubic meters
    annual_production_capacity = models.FloatField()  # Assuming in tons or units
    capital = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming in currency
    number_of_shares = models.PositiveIntegerField()
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming in currency


    def __str__(self):
        return self.name
    


class Projectpage(models.Model):
   
    proname = models.CharField(max_length=100,default= 'name')
    description = models.TextField(blank=True, null=True)
    projectlogo = models.ImageField(upload_to='project_logos/', max_length=200,default='images/profilepicdefalt.png',blank=True, null=True)
    prologoname = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.proname
    


class video(models.Model):
    video = models.FileField(upload_to='videos/', blank=True)
    videoname = models.CharField(max_length=50, blank=True, null=True)
    date_of_upload = models.DateField(max_length=50, blank=True, null=True)


class MyProject(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    projectlogo = models.ImageField(upload_to='projectlogo_attachments/',blank=True,null=True)
    projectlogoname =models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


    date_of_establishment = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    number_of_ponds = models.PositiveIntegerField(blank=True, null=True)
    water_capacity = models.FloatField(blank=True, null=True)  # Assuming in liters or cubic meters
    annual_production_capacity = models.FloatField(blank=True, null=True)  # Assuming in tons or units
    capital = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
    number_of_shares = models.PositiveIntegerField(blank=True, null=True)
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency

    investment_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
    investment_date = models.DateField(blank=True, null=True)
    receipt = models.FileField(upload_to='investment_receipts/', blank=True, null=True)
    installments = models.PositiveIntegerField(default=1,blank=True, null=True)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
    total_number_of_shares = models.PositiveIntegerField(blank=True, null=True)
    investment_price_per_share = models.DecimalField(max_digits=10, decimal_places=2)  # Assuming in currency
    shares_holding = models.PositiveIntegerField(default=0)
    share_certificate = models.FileField(upload_to='share_certificates/', blank=True, null=True)

    dividend_date = models.DateField(blank=True, null=True)
    dividend_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
    transfer_proof = models.FileField(upload_to='dividend_transfer_proof/', blank=True, null=True)
    total_dividend = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency

    partnership_agreement = models.FileField(upload_to='partnership_agreements/', blank=True, null=True)
    other_agreements = models.FileField(upload_to='other_agreements/', blank=True, null=True)

    project_images = models.ImageField(upload_to='project_images/', blank=True, null=True)
    project_videos = models.FileField(upload_to='project_videos/', blank=True, null=True)
    project_live = models.BooleanField(default=False)
   
    def __str__(self):
        return self.name









class OtherProject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')  # Field to store the image file
    uploaded_at = models.DateTimeField(default=timezone.now)  # Timestamp of when the image was uploaded

    def __str__(self):
        return str(self.image)




class JoinRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    project = models.ForeignKey('NewProject', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {self.status}"


from django.db import models



class AboutUsPage(models.Model):
    unix_aquatics = models.TextField(default=None)
    vision = models.TextField(default=None)
    mission = models.TextField(default=None)
    # team_unix = models.CharField(max_length=100, null=True)
    # contact_info_id=models.TextField(default=None)

    def __str__(self):
        return "About Us Page"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    photoname = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Team members"


class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return "ContactInfo"

class HomePageData(models.Model):
    banner_image = models.ImageField(upload_to='home_page')
    welcome_message = models.TextField()
    cta_button_text = models.CharField(max_length=50)
    cta_button_link = models.URLField()
    recent_updates_or_news = models.TextField()
    # social_media_links=models.TextField(default=None)
    # featured_content=models.TextField(default=None)
    def __str__(self):
        return "Home Page Data"


class Revenue(models.Model):
    
    project = models.ForeignKey(Projectpage, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Update total revenue for the project when saving a new revenue entry
        self.project.total_revenue += self.amount
        self.project.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Revenue for {self.project.name} - {self.amount}"

class Expense(models.Model):

    project = models.ForeignKey(Projectpage, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Update total expenses for the project when saving a new expense entry
        self.project.total_expenses += self.amount
        self.project.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Expense for {self.project.name} - {self.amount}"

