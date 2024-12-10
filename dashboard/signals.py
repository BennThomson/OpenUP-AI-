from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Billing_model
from datetime import datetime


@receiver(post_save, sender=Billing_model)
def set_expire_date(sender, instance, **kwargs):
    if instance.expire_date is None:
        paid_date_list = list(map(lambda x: int(x), str(instance.paid_date).split("-")))
        if instance.type == "Monthly":
            if paid_date_list[1] == 12:
                paid_date_list[0] += 1
                paid_date_list[1] = 1
            else:
                paid_date_list[1] += 1
            expire_date_obj = datetime(
                paid_date_list[0], paid_date_list[1], paid_date_list[2]
            ).date()
        else:
            paid_date_list[0] += 1
            expire_date_obj = datetime(
                paid_date_list[0], paid_date_list[1], paid_date_list[2]
            ).date()

        Billing_model.objects.filter(id=instance.id).update(expire_date=expire_date_obj)
