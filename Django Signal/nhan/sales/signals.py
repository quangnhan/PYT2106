from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Sale

@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, **kwargs):
    order = instance.order
    order.is_active = False
    order.save()
