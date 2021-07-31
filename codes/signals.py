from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Code


@receiver(post_save, sender=CustomUser)
def code_ganerat_(sender, instance, created, *args, **kwargs):
    if created:
        Code.objects.create(user=instance)
