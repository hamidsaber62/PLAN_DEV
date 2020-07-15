# -*- coding: utf-8 -*-
# import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
from datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@           PROCTOR_SURNAME
PROCTOR_SURNAME = (
    (1, 'معاون وزیر رئیس هیات مدیره و مدیر عامل'),
    (2, 'عضو هیات مدیر'),
    (3, 'معاون فنی و بازرگانی مدیر عامل'),
    (4, 'معاون فن اوری اطلاعات مدیر عامل'),
    (5, 'معاون پشتیبانی و توسعه مدیریت مدیر عامل'),
)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@           CARD_TYPE
CARD_TYPE = (
    (1, 'گروه های فعال در دفتر'),
    (2, 'برنامه ها و فعالیتهای سال جاری'),
    (3, 'مشخصات و سوابق فردی فردی مجری'),
    (4, 'توضیحات طرح'),
    (5, 'توضیحات پروژه'),
    (6, 'توضیحات زیر پروژه'),
    (7, 'توضیحات فعالیت مربوط به'),
)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@           PLAN

#   TODO: for PLAN_NAME create model AND form when insert final data
PLAN_NAME = (
    (1, 'طرح توسعه زیر ساخت'),
    (2, 'طرح کد پستی'),
    (3, 'طرح مقاوم سازی'),
    (4, 'طرح خدمات اجباری روستایی'),
    (5, 'طرح فن آوری'),
)
PLAN_TYPE = (
    (1, 'انتفاعی'),
    (2, 'غیر انتفاعی'),
)

ORGANIZATION = (
    (1, 'وزارت ارتباطات و فن آوری اطلاعات'),
)
BENEFICIARY = (
    (1, 'شرکت ملی پست'),
)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def picture_path(instance, filename):
    print('instance.name -->>', instance.name, 'filename -->>', filename)
    return "{0}{1}".format(instance.name, filename)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class InfoCard(models.Model):
    type = models.PositiveSmallIntegerField('نوع کارت', choices=CARD_TYPE,
                                            null=True)
    name = models.CharField('عنوان کارت', max_length=150, null=True)
    title = models.CharField('عنوان بازشو کارت', max_length=150, null=True)
    card_content = models.TextField('مطالب کارت', null=True)
    card_pic = models.ImageField(upload_to=picture_path,
                                 verbose_name='عکس کارت',
                                 help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                                 null=True)
    thumbnail_pic = models.ImageField(upload_to=picture_path,
                                      verbose_name='عکس بند انگشتی',
                                      help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                                      null=True)
    link_card_pic = models.CharField('لینک تصویر', max_length=100, blank=True,
                                     null=True)
    link_card_bottom = models.CharField('لینک ذیل مطلب روی کارت',
                                        max_length=100,
                                        blank=True, null=True)
    link_card_reveal = models.CharField('لینک قسمت بازشوی کارت', max_length=100,
                                        blank=True, null=True)
    link_action1 = models.CharField('لینک یکم', max_length=100, blank=True,
                                    null=True)
    link_action2 = models.CharField('لینک دوم', max_length=100, blank=True,
                                    null=True)
    link_action3 = models.CharField('لینک سوم', max_length=100, blank=True,
                                    null=True)

    def __str__(self):
        return "{}".format(self.name)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class AttachmentFile(models.Model):
    file = models.FileField(
        upload_to="attachment_file/{0}".format("%Y-%m-%d_%H-%M"))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_name = models.CharField(max_length=155, null=True, blank=True)
    content_object = GenericForeignKey()

    def __str__(self):
        # return "مستندات {}".format(self.content_object.name)
        return "مستندات {}".format(self.object_name)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class ImageGallery(models.Model):
    objects = None
    name = models.CharField('عنوان تصویر', max_length=100, blank=True,
                            null=True)
    alt = models.CharField('alt', max_length=100, blank=True, null=True)
    link = models.CharField('لینک تصویر', max_length=100, blank=True, null=True)
    pic = models.ImageField(upload_to=picture_path, verbose_name='ذخیره تصویر',
                            help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                            blank=True, null=True)
    description = models.TextField('توضیحات ضروری تصویر', blank=True, null=True)

    def __str__(self):
        return self.name

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class Project(models.Model):
    objects = None
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE,
                             verbose_name='نام طرح')
    name = models.CharField('نام پروژه', max_length=255, unique=True)
    number = models.CharField('شماره پروژه', max_length=15, unique=True,
                              blank=True, null=True)
    start_date = models.DateField('تاریخ شروع پروژه', blank=True, null=True)
    end_date = models.DateField('تاریخ خاتمه پروژه', blank=True, null=True)
    entry_datetime = models.DateTimeField('تاریخ و زمان ثبت ', blank=True,
                                          null=True)
    credit = models.IntegerField('اعتبار مصوب پروژه',
                                 help_text='عدد را بدون ممیز اعشاری وارد نمایید(میلیون ریال)',
                                 default=0, blank=True, null=True)
    description = models.TextField('توضیحات ضروری پروژه', null=True)
    attachment_file = GenericRelation('AttachmentFile')

    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return "{0} Registered by operator >> {2}  ; From {1}".format(self.project_name, self.plan, self.user)
        return "پروژه {0}".format(self.name)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   TODO: for PLAN_NAME create model AND form when insert final data

class Plan(models.Model):
    objects = None
    plan = 'طرح'
    name = models.PositiveSmallIntegerField('عنوان طرح', choices=PLAN_NAME,
                                            help_text='یکی از عناوین از پیش درج شده را انتخاب و ثبت نمایید',
                                            unique=True, blank=True, null=True)
    organization = models.PositiveSmallIntegerField('عنوان دستگاه اجرایی',
                                                    choices=ORGANIZATION,
                                                    blank=True, null=True)
    number = models.CharField('شماره طرح', max_length=255, unique=True,
                              blank=True, null=True)
    beneficiary = models.PositiveSmallIntegerField('عنوان دستگاه بهره بردار',
                                                   choices=BENEFICIARY,
                                                   blank=True,
                                                   null=True)
    beneficiary_code = models.CharField('شماره دستگاه بهره بردار',
                                        max_length=15, blank=True, null=True)
    type = models.PositiveSmallIntegerField('نوع طرح', choices=PLAN_TYPE,
                                            blank=True, null=True)
    project_quantity = models.IntegerField('تعداد پروژه ها', blank=True,
                                           null=True)
    start_date = models.DateField('تاریخ شروع طرح', blank=True, null=True)
    end_date = models.DateField('تاریخ خاتمه طرح', blank=True, null=True)
    entry_datetime = models.DateTimeField('تاریخ و زمان ثبت ', blank=True,
                                          null=True)
    credit = models.IntegerField('اعتبار مصوب طرح',
                                 help_text='عدد را بدون ممیز اعشاری وارد نمایید(میلیون ریال)',
                                 default=0, blank=True, null=True)
    description = models.TextField('توضیحات ضروری طرح', null=True)
    attachment_file = GenericRelation('AttachmentFile', null=True)

    @property
    def plan_index(self):
        p_nam = dict(PLAN_NAME)[self.name]
        typ = dict(PLAN_TYPE)[self.type]
        return p_nam, typ
    nam = plan_index

    def __str__(self):
        # return "{0}".format(self.plan_index[0])
        return "{0}".format(self.nam[0])

    # plan_file = models.FileField('مستندات', upload_to='plan_file/%Y_%m%d_%H%M', blank=True, null=True)

    #
    #     # user = models.ForeignKey(User, on_delete=models.CASCADE)
    #     # def was_recently(self):
    #     #     return self.entry_datetime >= timezone.now() - timezone.timedelta(days=1)
    #
    #     def get_absolute_url(self):
    #
    #         return reverse('pages:about', args=[str(self.name)])
    #


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class Proctor(models.Model):
    objects = None
    Proctor = 'مجری طرح'
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,
                             verbose_name='انتخاب طرح')
    name = models.CharField('نام مجری', max_length=100, unique=True)
    # surname = ('man', 'معاون وزیر رئیس هیات مدیره و مدیر عامل'), ('ma2', 'عضو هیات مدیر'), \
    #           ('as1', 'معاون فنی و بازرگانی مدیر عامل'), ('as2', 'معاون فن اوری اطلاعات مدیر عامل'), \
    #           ('as3', 'معاون پشتیبانی و توسعه مدیریت مدیر عامل')
    surname = models.PositiveSmallIntegerField('عنوان مجری',
                                               choices=PROCTOR_SURNAME,
                                               null=True)
    entry_datetime = models.DateTimeField('تاریخ و زمان ثبت ', null=True)
    pic = models.ImageField(upload_to=picture_path, verbose_name='عکس پرسنلی',
                            help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                            null=True)
    description = models.TextField('توضیحات ضروری مجری', null=True)

    # position = models.CharField('سمت اداری مجری', max_length=255, null=True, blank=True)
    @property
    def proctor_index(self):
        surname = dict(PROCTOR_SURNAME)[self.surname]
        return surname

    def __str__(self):
        return "مجری {}".format(self.name)


# @@@@@@@@@@@@@@@@                              @@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@                      @@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


date_now = timezone.now()
# date_now = datetime.now()
print('#############################################')
print('#############################################')
print('timezone.now() =', timezone.now())
print('#############################################')
print('#############################################')
print('timezone.now() =', datetime.now())
print('#############################################')
print('#############################################')
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
