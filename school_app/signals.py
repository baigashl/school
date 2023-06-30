from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=Student)
def send_student_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to School!'
        message = f'Dear {instance.full_name}, welcome to our school!'
        send_mail(subject, message, 'baigashkaevi02@gmail.com', [instance.email])
