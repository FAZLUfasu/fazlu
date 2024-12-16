# In signals.py (or a new file)

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from fazlu.fasu.admin import UserAdmin

@receiver(post_save, sender=UserAdmin)  # Use your User model here
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome!',
            'Thank you for registering.',
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
