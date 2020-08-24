# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
from sa_account_app.models import UserProfile
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime
from khayyam import JalaliDatetime, TehranTimezone
from rtl import rtl


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey()
    create_chat_datetime = models.DateTimeField(auto_now_add=True, null=True)
    seen = models.BooleanField(default=False, null=True)
    seen_datetime = models.DateTimeField(null=True, blank=True)

    def jd_create_chat(self):
        jd_datetime = JalaliDatetime(datetime(year=self.create_chat_datetime.year,
                                              month=self.create_chat_datetime.month,
                                              day=self.create_chat_datetime.day,
                                              hour=self.create_chat_datetime.hour,
                                              minute=self.create_chat_datetime.minute,
                                              second=self.create_chat_datetime.second, ))
        year = jd_datetime.year
        month = jd_datetime.month
        day = jd_datetime.day
        hour = jd_datetime.hour
        minute = jd_datetime.minute
        second = jd_datetime.second
        # print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', '\n',
        #       JalaliDatetime(year, month, day, hour, minute, second).strftime(' %A %d %B  %Y'))
        return JalaliDatetime(year, month, day, hour, minute, second).strftime(" %A %d %B  %Y-  ساعت %H:%M:%S")

    def is_manager(self):
        return 'manager' in [usr_g.name for usr_g in self.user.groups.all()]

    def is_operator(self):
        # return 'manager' in [usr_g.name for usr_g in self.user.groups.all()]
        #     OR
        return not self.is_manager()

    def __str__(self):
        return '{0}'.format(self.message[:30])
