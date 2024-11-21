
from django.contrib import admin
from .models import AboutUs, ContactInfo, InvestorProfile, MyProjects, NewsUpdate, Notification,Summary
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import InvestorProfile,Images,Projectpage, TeamMember, video
from django.contrib import admin
from .models import Join

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "INVESTERS APP"  # default: "Django Administration"
admin.site.site_title = "UNIX"  # default: "Django site admin"
admin.site.index_title = "Admin"  # default: "Site administration"



admin.site.register(Join)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(video)
admin.site.register(AboutUs)
admin.site.register(ContactInfo)
admin.site.register(TeamMember)
admin.site.register(Summary)
admin.site.register(Images)
admin.site.register(Notification)



@admin.register(NewsUpdate)
class NewsUpdateAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_published']
    search_fields = ['title', 'description']
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  


class InvestorProfileInline(admin.StackedInline):
    model = InvestorProfile
    can_delete = False
    verbose_name_plural = 'Investor Profiles'
    extra = 1
    max_num = 1
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  


class MyProjectsInline(admin.StackedInline):
    model = MyProjects
    can_delete =False
    verbose_name_plural = 'My Project'
    extra = 6
    max_num = 6
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  



class CustomUserAdmin(UserAdmin):
    inlines = (InvestorProfileInline,)
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  


class CustomProjectpageAdmin(Projectpage):
    inlines = (MyProjectsInline,)

    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  



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

    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  


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
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  


# Re-register UserAdmin
class ProjectpageInline(admin.StackedInline):
    model = Projectpage
    fields = ['proname']  # List of fields from Projectpage to display
    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = ('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')  



admin.site.register(MyProjects)
class MyProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectpageInline]
    list_display = ['user', 'projectlogoname', 'projectlogo', 'get_proname']

    def get_proname(self, obj):
        return obj.name.proname if obj.name else ''  # Custom method to display proname
    get_proname.short_description = 'Project Name'





    class Media:
        css = {'all': ('admin/custom.css',)  }
        js = {'all':('admin/custom.js','admi/jquery-3.4.1.min.js','admin/bootstrap.js')}  

