
from django.contrib import admin
from .models import ContactInfo, Expense, HomePageData, InvestorProfile, JoinRequest, MyProject, NewProject, OtherProject 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import InvestorProfile,AboutUsPage,Image,Projectpage, Revenue, TeamMember, video

admin.site.register(NewProject)
admin.site.register(OtherProject)
admin.site.register(video)
admin.site.register(Revenue)
admin.site.register(Expense)
admin.site.register(JoinRequest)
admin.site.register(HomePageData)
admin.site.register(AboutUsPage)
admin.site.register(ContactInfo)
admin.site.register(TeamMember)
admin.site.register(Image)


class InvestorProfileInline(admin.StackedInline):
    model = InvestorProfile
    can_delete = False
    verbose_name_plural = 'Investor Profiles'
    extra = 1
    max_num = 1
class MyProjectInline(admin.StackedInline):
    model = MyProject
    can_delete =False
    verbose_name_plural = 'My Project'
    extra = 6
    max_num = 6
    

class CustomUserAdmin(UserAdmin):
    inlines = (InvestorProfileInline,)

class CustomProjectpageAdmin(Projectpage):
    inlines = (MyProjectInline,)


admin.site.register(MyProject)
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
            # Only allow updating existing profile
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



# @admin.register(NewProject)
# class NewProjectAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'location', 'start_date', 'end_date', 'date_of_establishment')

