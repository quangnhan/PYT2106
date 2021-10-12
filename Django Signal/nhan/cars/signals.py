from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Car

@receiver(pre_save, sender=Car)
def pre_save_car(sender, instance, **kwagrs):
    print("------- Pre save -------")
    print(instance)
    print(Car.objects.all())

@receiver(post_save, sender=Car)
def post_save_car(sender, instance, created, **kwagrs):
    print("------- Post save -------")
    print(instance)
    print(Car.objects.all())

@receiver(pre_delete, sender=Car)
def pre_delete_car(sender, instance, **kwagrs):
    print("------- Pre delete -------")
    print(instance)
    print(Car.objects.all())

@receiver(post_delete, sender=Car)
def post_delete_car(sender, instance, **kwagrs):
    print("------- Post delete -------")
    print(instance)
    print(Car.objects.all())