
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# for shell
#     from django.contrib.auth.models import User
#     from sa_account_app.models import UserProfile
#     user=User.objects.get(username='admin')
#     prof=UserProfile.objects.get(user=user)

ROLE_CHOICES = (
    (1, 'فقط مشاهده'),
    (2, 'نظارت و رفع مغایرت'),
    (3, 'متصدی ثبت و پاسخگوئی'),
    (4, 'مدیر اجرائی و ناظر نهائی'),
    (5, 'مجری و مدیر کل سیستم'),
)
LOCATION_JOB = (
    (1, 'حوزه معاونت فنی و بازرگانی'),
    (2, 'حوزه معاونت فن اوری اطلاعات و تجارت الکترونیک'),
    (3, 'حوزه معاونت پشتیبانی و توسعه مدیریت'),
    (4, 'اعضاء هیات مدیر'),
    (5, 'معاون وزیر رئیس هیات مدیره و مدیر عامل'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    location_job = models.PositiveSmallIntegerField(choices=LOCATION_JOB, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    @property
    def user_role(self):
        # import ipdb; ipdb.set_trace()
        user_role = dict(ROLE_CHOICES)[self.role]
        return user_role

    @property
    def user_location(self):
        # import ipdb; ipdb.set_trace()
        user_location = dict(LOCATION_JOB)[self.location_job]
        return user_location

    # TODO complete setter for role AND location job

    @user_role.setter
    def user_role(self, new_role):
        revers_role_dict = {v: k for k, v in dict(ROLE_CHOICES).items()}
        self.role = revers_role_dict.get(new_role)

    @user_location.setter
    def user_location(self, new_location):
        revers_location_dict = {v: k for k, v in dict(LOCATION_JOB).items()}
        self.location_job = revers_location_dict.get(new_location)

    def __str__(self):  # __unicode__ for Python 2
        return "{0} _{1} __{2}___{3}".format(self.user.username, self.role, self.location_job, self.phone)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
