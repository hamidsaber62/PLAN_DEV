from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICES = (
    (1, 'فقط مشاهده'),
    (2, 'نظارت و رفع مغایرت'),
    (3, 'متصدی ثبت و پاسخگوئی'),
    (4, 'مدیر اجرائی و ناظر نهائی'),
    (5, 'مجری و مدیر کل سیستم'),
)
LOCATION = (
    (1, 'حوزه معاونت فنی و بازرگانی'),
    (2, 'حوزه معاونت فن اوری اطلاعات و تجارت الکترونیک'),
    (3, 'حوزه معاونت پشتیبانی و توسعه مدیریت'),
    (4, 'اعضاء هیات مدیر'),
    (5, 'معاون وزیر رئیس هیات مدیره و مدیر عامل'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    location = models.PositiveSmallIntegerField(choices=LOCATION, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()
