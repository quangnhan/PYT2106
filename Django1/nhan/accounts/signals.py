from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string

@receiver(post_save, sender=get_user_model())
def post_save_user(sender, instance, created, **kwagrs):
    if created: 
        data = {
            "last_name": instance.last_name,
            "first_name": instance.first_name,
        }
        messages = render_to_string('email/welcome.html', data)
        send_mail(
            'Chào mừng bạn đến với khóa học lập trình Django',
            messages,
            None,
            [instance.email]
        )