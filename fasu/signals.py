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
