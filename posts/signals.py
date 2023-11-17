from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.models import User



from rest_framework.authtoken.models import Token

from drf_assignment import settings
from posts.models import Posts




@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=Posts)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        subject = 'New Post Created'
        from_email = settings.DEFAULT_EMAIL_FROM 
        html_message = render_to_string('email/notification.html', {'post': instance})
        to_email = instance.author.email
        send_mail(subject, html_message, from_email, [to_email])
        print('mail sent')
        