
from rest_framework.authtoken.models import Token
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class NewsUpdate(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Login(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # username = models.CharField(max_length=50,default=None)
    # email = models.EmailField(max_length=50,blank=True, null=True,default=None)
    # password = models.CharField(max_length=50,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Summary(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class InvestorProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    profilepic = models.ImageField(upload_to='profilpic_attachments/',blank=True,)
    profilepicname =models.CharField(max_length=50, blank=True, null=True)
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
  
    # id= models.CharField(max_length=100,blank=True, null=True)
   
    def __str__(self):
        return self.name





# class Projectpage(models.Model):
   
#     id = models.AutoField(primary_key=True) 
#     proname = models.CharField(unique=True,max_length=100,default='name')
#     description = models.TextField(blank=True, null=True)
#     projectlogo = models.ImageField(upload_to='project_logos/', max_length=200,default='images/profilepicdefalt.png',blank=True, null=True)
#     prologoname = models.TextField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     date_of_establishment = models.DateField(blank=True, null=True)
#     location = models.CharField(max_length=100,blank=True, null=True)
#     number_of_ponds = models.PositiveIntegerField(blank=True, null=True)
#     water_capacity = models.FloatField(blank=True, null=True)  # Assuming in liters or cubic meters
#     annual_production_capacity = models.FloatField(blank=True, null=True)  # Assuming in tons or units
#     capital = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     number_of_shares = models.PositiveIntegerField(blank=True, null=True)
#     price_per_share = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency

    
#     def __str__(self):
#         return self.proname
    


# class MyProjects(models.Model):


#     id= models.AutoField(primary_key=True) 
#     project = models.CharField(max_length=50, blank=True, null=True)
#     proname = models.ForeignKey(Projectpage, on_delete=models.CASCADE, related_name='projects', default=None)    
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
#     projectlogo = models.ImageField(upload_to='projectlogo_attachments/',blank=True)
#     projectlogoname =models.CharField(max_length=50, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True,default=None)
#     end_date = models.DateField(blank=True, null=True,default=None)

   
#     date_of_establishment = models.DateField()
#     location = models.CharField(max_length=100,default=None)
#     number_of_ponds = models.PositiveIntegerField(blank=True, null=True)
#     water_capacity = models.FloatField(blank=True, null=True)  # Assuming in liters or cubic meters
#     annual_production_capacity = models.FloatField(blank=True, null=True)  # Assuming in tons or units
#     capital = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     number_of_shares = models.PositiveIntegerField(blank=True, null=True)
#     price_per_share = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     investment_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     investment_date = models.DateField(blank=True, null=True)
#     receipt = models.FileField(upload_to='investment_receipts/', blank=True, null=True)
   
#     installments = models.PositiveIntegerField(default=1,blank=True, null=True)
#     total_investment = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     total_number_of_shares = models.PositiveIntegerField(blank=True, null=True)
#     investment_price_per_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Assuming in currency
#     shares_holding = models.PositiveIntegerField(default=0, blank=True, null=True)
#     share_certificate = models.FileField(upload_to='share_certificates/', blank=True, null=True)


#     dividend_date = models.DateField(blank=True, null=True)
#     dividend_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     transfer_proof = models.FileField(upload_to='dividend_transfer_proof/', blank=True, null=True)
#     total_dividend = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)  # Assuming in currency
#     partnership_agreement = models.FileField(upload_to='partnership_agreements/', blank=True, null=True)
#     other_agreements = models.FileField(upload_to='other_agreements/', blank=True, null=True)

   
#     def __str__(self):
#       return f'{self.user.username} - {self.proname.proname}'


class BaseProject(models.Model):
    description = models.TextField(blank=True, null=True)
    projectlogo = models.ImageField(upload_to='project_logos/', max_length=200, default='images/profilepicdefalt.png', blank=True, null=True)
    projectlogoname = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    date_of_establishment = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    number_of_ponds = models.PositiveIntegerField(blank=True, null=True)
    water_capacity = models.FloatField(blank=True, null=True)
    annual_production_capacity = models.FloatField(blank=True, null=True)
    capital = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    number_of_shares = models.PositiveIntegerField(blank=True, null=True)
    price_per_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        abstract = True


class Projectpage(BaseProject):
    id = models.AutoField(primary_key=True)
    proname = models.CharField(unique=True, max_length=100, default='name')

    def __str__(self):
        return self.proname



class MyProjects(BaseProject):
    id = models.AutoField(primary_key=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    proname = models.ForeignKey(Projectpage, on_delete=models.CASCADE, related_name='projects', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Change to ForeignKey
    end_date = models.DateField(blank=True, null=True, default=None)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    investment_date = models.DateField(blank=True, null=True)
    receipt = models.FileField(upload_to='investment_receipts/', blank=True, null=True)
    installments = models.PositiveIntegerField(default=1, blank=True, null=True)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_number_of_shares = models.PositiveIntegerField(blank=True, null=True)
    investment_price_per_share = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shares_holding = models.PositiveIntegerField(default=0, blank=True, null=True)
    share_certificate = models.FileField(upload_to='share_certificates/', blank=True, null=True)
    dividend_date = models.DateField(blank=True, null=True)
    dividend_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transfer_proof = models.FileField(upload_to='dividend_transfer_proof/', blank=True, null=True)
    total_dividend = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    partnership_agreement = models.FileField(upload_to='partnership_agreements/', blank=True, null=True)
    other_agreements = models.FileField(upload_to='other_agreements/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.proname.proname}'



class video(models.Model):
    message = models.CharField(max_length=255, default='New video uploaded',blank=True, null=True)
    video = models.FileField(upload_to='videos/')
    videoname = models.CharField(max_length=50, blank=True, null=True)
    date_of_upload = models.DateField(max_length=50, blank=True, null=True)
    def __str__(self):
            return str(self.videoname)

 

    
class Images(models.Model):

    message = models.CharField(max_length=255, default='New image uploaded',blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    imagename = models.CharField(max_length=100,blank=True, null=True) 
    uploaded_at = models.DateTimeField(default=timezone.now) 


    def __str__(self):
         return self.imagename
    

    
class Notification(models.Model):
    message = models.CharField(max_length=255)
    last_uploaded_image_id = models.IntegerField(default=0)

@receiver(post_save, sender=Images)
def create_notification(sender, instance, **kwargs):
    last_uploaded_image_id = instance.id
    notification = Notification.objects.first()
    if notification:
        notification.last_uploaded_image_id = last_uploaded_image_id
        notification.save()
    else:
        Notification.objects.create(message='New image uploaded', last_uploaded_image_id=last_uploaded_image_id)
        
class VideoNotification(models.Model):
    message = models.CharField(max_length=255)
    last_uploaded_video_id = models.IntegerField(default=0)
    
@receiver(post_save, sender=video)
def create_video_notification(sender, instance, **kwargs):
    last_uploaded_video_id = instance.id
    videonotification = Notification.objects.first()
    if videonotification:
        videonotification.last_uploaded_video_id = last_uploaded_video_id
        videonotification.save()
    else:
        Notification.objects.create(message='New video uploaded', last_uploaded_video_id=last_uploaded_video_id)



class Join(models.Model):
    username = models.CharField(max_length=100,default=None)
    projectname = models.CharField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} requests to join {self.projectname}"

class AboutUs(models.Model):
    unix_aquatics = models.TextField(default=None)
    vision = models.TextField(default=None)
    mission = models.TextField(default=None)
    

    def __str__(self):
        return "About Us"

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team_photos/')
    photoname = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)


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



class Whatsappchat(models.Model):
    phone_number = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.phone_number




class backgroundimage(models.Model):
    id = models.AutoField(primary_key=True)
    bg_image = models.ImageField(upload_to='bg_image')
    
    def __str__(self):
        return "backgroundimage"
