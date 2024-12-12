
from django.contrib import admin
from .models import AboutUs, BackgroundImage, ContactInfo, InvestorProfile, MyProjects, NewsUpdate, Notification,Summary, VideoNotification
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import InvestorProfile,Images,Projectpage, TeamMember, video
from django.contrib import admin
from .models import Join
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.conf import settings


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "INVESTERS APP"  # default: "Django Administration"
admin.site.site_title = "UNIX"  # default: "Django site admin"
admin.site.index_title = "Admin"  # default: "Site administration"

admin.site.register(BackgroundImage)

admin.site.register(Join)

admin.site.register(video)
admin.site.register(AboutUs)
admin.site.register(ContactInfo)
admin.site.register(TeamMember)
admin.site.register(Summary)
admin.site.register(Images)
admin.site.register(Notification)
admin.site.register(VideoNotification)



# @admin.action(description='Reset selected user passwords')
# def reset_user_password(modeladmin, request, queryset):
#     # This action will send a reset password email to selected users
#     for user in queryset:
#         # Create a password reset link
#         uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})

#         # Create the email message
#         reset_url = f"{settings.SITE_URL}{reset_link}"
#         subject = "Password Reset Request"
#         message = render_to_string('registration/password_reset_email.html', {
#             'user': user,
#             'reset_url': reset_url
#         })

#         # Send the reset password email
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
#     actions = [reset_user_password]  # Add the custom action here

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_published']
    search_fields = ['title', 'description']



class InvestorProfileInline(admin.StackedInline):
    model = InvestorProfile
    can_delete = False
    verbose_name_plural = 'Investor Profiles'
    extra = 1
    max_num = 1
 

class MyProjectsInline(admin.StackedInline):
    model = MyProjects
    can_delete =False
    verbose_name_plural = 'My Project'
    extra = 6
    max_num = 6


class CustomUserAdmin(UserAdmin):
    inlines = (InvestorProfileInline,)


class CustomProjectpageAdmin(Projectpage):
    inlines = (MyProjectsInline,)

    


admin.site.register(Projectpage)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(InvestorProfile)
class InvestorProfileAdmin(admin.ModelAdmin):

    list_display = '__all__' # Fields to display in the admin list view
    search_fields = ['name', 'email', 'mobile_number']  # Enable search by name, email, and mobile number
    list_filter = ['account_number', 'bank_name']  # Add filters for account number and bank name
    list_per_page = 20  # Number of items to display per page
    fieldsets = (
        ('Personal Information', {
            'fields': ('user', 'name', 'address', 'mobile_number', 'email', 'whatsapp', 'profilepic'),
        }),
        ('Identity Documents', {
            'fields': ('aadhar_card', 'aadhar_card_attachment', 'election_id', 'election_id_attachment', 'passport_number', 'passport_attachment', 'pan_card_number', 'pan_card_attachment'),
        }),
        ('Bank Information', {
            'fields': ('account_number', 'iban', 'bank_name', 'branch', 'ifsc_code', 'bank_account_passbook_attachment'),
        }),
    )
    readonly_fields = ['user', 'email']  # Fields that should be read-only in the admin interface
    # Add other configurations as needed

    def save_model(self, request, obj, form, change):
        # Check if a profile already exists for the user
        if not InvestorProfile.objects.filter(user=obj.user).exists():
            super().save_model(request, obj, form, change)
        else:
            # Only allow updating existing profilez
            if change:
                super().save_model(request, obj, form, change)
            else:
                # Prevent creating a new profile for the same user
                # You can customize the error message as per your requirement
                raise ValueError("Profile already exists for this user.")
    
    def has_add_permission(self, request):
        # Only allow admins to add user profiles
        return request.user.is_superuser or request.user.is_staff

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Limit the choices for the user field to admin users and superusers
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

   

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
  


class ProjectpageInline(admin.StackedInline):
    model = Projectpage
    fields = ['proname']  # List of fields from Projectpage to display
  

admin.site.register(MyProjects)
class MyProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectpageInline]
    list_display = ['user', 'projectlogoname', 'projectlogo', 'get_proname']

    def get_proname(self, obj):
        return obj.name.proname if obj.name else ''  # Custom method to display proname
    get_proname.short_description = 'Project Name'




