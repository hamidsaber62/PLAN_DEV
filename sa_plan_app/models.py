
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
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
from django.urls import reverse
from sa_chat_app.models import Chat
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# @@@@@@@@@@@@@@@@@@@@@@@@@@@           PROCTOR_SURNAME
PROCTOR_SURNAME = [
    (1, 'معاون وزیر رئیس هیات مدیره و مدیر عامل'),
    (2, 'عضو هیات مدیر'),
    (3, 'معاون فنی و بازرگانی مدیر عامل'),
    (4, 'معاون فن اوری اطلاعات مدیر عامل'),
    (5, 'معاون پشتیبانی و توسعه مدیریت مدیر عامل'),
]
# @@@@@@@@@@@@@@@@@@@@@@@@@@@           CARD_TYPE
CARD_TYPE = [
    (1, 'گروه های فعال در دفتر'),
    (2, 'برنامه ها و فعالیتهای سال جاری'),
    (3, 'مشخصات و سوابق فردی فردی مجری'),
    (4, 'توضیحات طرح'),
    (5, 'توضیحات پروژه'),
    (6, 'توضیحات زیر پروژه'),
    (7, 'توضیحات فعالیت مربوط به'),
]
# @@@@@@@@@@@@@@@@@@@@@@@@@@@           PLAN

#   TODO: for PLAN_NAME create model AND UI_form when insert final data
PLAN_NAME = [
    (1, 'طرح توسعه زیر ساخت'),
    (2, 'طرح کد پستی'),
    (3, 'طرح مقاوم سازی'),
    (4, 'طرح خدمات اجباری روستایی'),
    (5, 'طرح فن آوری'),
]
PLAN_TYPE = [
    (1, 'انتفاعی'),
    (2, 'غیر انتفاعی'),
]

ORGANIZATION = [
    (1, 'وزارت ارتباطات و فن آوری اطلاعات'),
]
BENEFICIARY = [
    (1, 'شرکت ملی پست'),
]


# @@@@@@@@@@@@@@@@@@@@@@@@@@@


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def picture_path(instance, filename):
    print('instance.name -->>', instance.name, 'filename -->>', filename)
    return "{0}{1}".format(instance.name, filename)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class InfoCard(models.Model):
    """
    برای پر کردن اتوماتیک "فیلد اسلگ" با تاسی از اسکریپت "fake_fill_DB" یک اسکریپت ساختم به نام "slugplan"
    که به خوبی نیز کار کرد دو روش دیگر هم هست یکی فانکشن یا تابع "save" که الان اضافه کردم و دیگری از پکیجهای آماده پایتون به نام"autoslug"
    """
    card_type = models.PositiveSmallIntegerField('نوع کارت', choices=CARD_TYPE,
                                                 null=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, blank=True)
    name = models.CharField('عنوان کارت', max_length=150, null=True)
    title = models.CharField('عنوان بازشو', max_length=150, null=True)
    card_content = models.CharField('مطلب روی کارت', max_length=150, null=True)
    card_description = models.TextField('توضیحات', null=True)
    card_pic = models.ImageField(upload_to=picture_path,
                                 verbose_name='عکس کارت',
                                 help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                                 null=True, blank=True)

    link_card_pic = models.CharField('لینک تصویر', max_length=100, blank=True,
                                     null=True)
    link_card_bottom = models.CharField('لینک اطلاعات تکمیلی(فیلد توضیحات)',
                                        max_length=100,
                                        blank=True, null=True)
    chat = GenericRelation(Chat)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # به این فیلدها با توجه به نوع کارتی که فعلا استفاده میکنم نیازی نیست

    # thumbnail_pic = models.ImageField(upload_to=picture_path,
    #                                   verbose_name='عکس بند انگشتی',
    #                                   help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
    #                                   null=True, blank=True)
    #
    # link_card_reveal = models.CharField('لینک قسمت بازشوی کارت', max_length=100,
    #                                     blank=True, null=True)
    # link_action1 = models.CharField('لینک یکم', max_length=100, blank=True,
    #                                 null=True)
    # link_action2 = models.CharField('لینک دوم', max_length=100, blank=True,
    #                                 null=True)
    # link_action3 = models.CharField('لینک سوم', max_length=100, blank=True,
    #                                 null=True)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @property
    def type_card(self):
        type_card = dict(CARD_TYPE)[self.card_type]
        return type_card

    @type_card.setter
    def type_card(self, new_type):
        revers_dict = {v: k for k, v in dict(CARD_TYPE).items()}
        self.card_type = revers_dict.get(new_type)

    def get_absolute_url(self):
        params = {'card_slug': self.slug}
        return reverse('sa_plan_app:more-info', kwargs=params)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(InfoCard, self).save(*args, **kwargs)

    def __str__(self):
        return "{0}--{1}".format(self.type_card, self.name)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class AttachmentFile(models.Model):
    file = models.FileField(
        upload_to="attachment_file/{0}".format("%Y-%m-%d_%H-%M"))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    object_name = models.CharField(max_length=155, null=True, blank=True)
    content_object = GenericForeignKey()

    @property
    def name(self):
        # return self.file.url.split('/')[-1]
        return self.content_object.name, self.file.url.split('/')[-1]

        # return '123'

    @property
    def color(self):
        colors = {
            'pptx': 'red lighten-1',
            'ppt': 'red lighten-1',
            'pdf': 'red accent-1',
            'xlsx': 'teal accent-3',
            'xls': 'teal accent-3',
            'csv': 'green',
            'txt': 'green accent-3',
            'docx': 'blue darken-2',
            'doc': 'blue darken-2',
            'rar': 'red darken-2',
            'zip': 'red darken-2',
            '7-zip': 'red darken-2',
            'py': 'yellow',
        }
        file_extension = self.name[1].split('.')[-1]
        return colors.setdefault(file_extension, 'grey')

    def get_absolute_url(self):
        params = {self.content_type.name, self.object_id}
        return reverse('sa_plan_app:plan-description', kwargs=params)

    def __str__(self):
        return "{0}".format(self.name)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class ImageGallery(models.Model):
    objects = None
    name = models.CharField('عنوان تصویر', max_length=100, blank=True,
                            null=True)
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, blank=True)
    alt = models.CharField('alt', max_length=100, blank=True, null=True)
    link = models.CharField('لینک تصویر', max_length=100, blank=True, null=True)
    pic = models.ImageField(upload_to=picture_path, verbose_name='ذخیره تصویر',
                            help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                            blank=True, null=True)
    description = models.CharField('مطلب روی تصویر', max_length=150, blank=True, null=True)
    chat = GenericRelation(Chat)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(ImageGallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
class Project(models.Model):
    objects = None
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE,
                             verbose_name='نام طرح')
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, blank=True)
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
    chat = GenericRelation(Chat)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        # return "{0} Registered by operator >> {2}  ; From {1}".format(self.project_name, self.plan, self.user)
        return "{0}".format(self.name)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   TODO: for dict PLAN_NAME create model AND UI_form when insert final data
class Plan(models.Model):
    objects = None
    plan = 'طرح'
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, blank=True)
    key_plan_name = models.PositiveSmallIntegerField('عنوان طرح', choices=PLAN_NAME,
                                                     help_text='یکی از عناوین از پیش درج شده را انتخاب و ثبت نمایید',
                                                     unique=True, blank=True, null=True)
    plan_organization = models.PositiveSmallIntegerField('عنوان دستگاه اجرایی',
                                                         choices=ORGANIZATION,
                                                         blank=True, null=True)
    number = models.CharField('شماره طرح', max_length=255, unique=True,
                              blank=True, null=True)
    plan_beneficiary = models.PositiveSmallIntegerField('عنوان دستگاه بهره بردار',
                                                        choices=BENEFICIARY,
                                                        blank=True,
                                                        null=True)
    beneficiary_code = models.CharField('شماره دستگاه بهره بردار',
                                        max_length=15, blank=True, null=True)
    plan_type = models.PositiveSmallIntegerField('نوع طرح', choices=PLAN_TYPE,
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
    chat = GenericRelation(Chat)

    @property
    #   در اینجه کلید دیکشنری را که یک عدد است میدهیم و نام طرح را میگیریم اینجا گتر است
    def name(self):
        name = dict(PLAN_NAME)[self.key_plan_name]
        return name

    @property
    def organization(self):
        organization = dict(ORGANIZATION)[self.plan_organization]
        return organization

    @property
    def beneficiary(self):
        beneficiary = dict(BENEFICIARY)[self.plan_beneficiary]
        return beneficiary

    @property
    def type_plan(self):
        type_plan = dict(PLAN_TYPE)[self.plan_type]
        return type_plan

    @name.setter
    #   در اینجا بر عکس تابع بالا عمل میکینیم نام طرح را میدهیم و عدد را میگیریم اینجا ستر است
    def name(self, new_name):
        revers_key_plan_name = {v: k for k, v in dict(PLAN_NAME).items()}
        self.key_plan_name = revers_key_plan_name.get(new_name)

    @organization.setter
    def organization(self, new_organization):
        revers_organization_dict = {v: k for k, v in dict(ORGANIZATION).items()}
        self.plan_organization = revers_organization_dict.get(new_organization)

    @beneficiary.setter
    def beneficiary(self, new_beneficiary):
        revers_beneficiary_dict = {v: k for k, v in dict(BENEFICIARY).items()}
        self.plan_beneficiary = revers_beneficiary_dict.get(new_beneficiary)

    @type_plan.setter
    def type_plan(self, new_type_plan):
        revers_type_plan_dict = {v: k for k, v in dict(PLAN_TYPE).items()}
        self.plan_type = revers_type_plan_dict.get(new_type_plan)

    def get_absolute_url(self):
        params = {'plan_slug': self.slug, 'plan_id': self.id}
        return reverse('sa_plan_app:plan-description', kwargs=params)

    # def get_absolute_url(self):
    #     params = {'plan_name': self.name, 'plan_id': self.id}
    #     return reverse('sa_plan_app:plan-description', kwargs=params)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(Plan, self).save(*args, **kwargs)

    def __str__(self):
        # name = self.name_plan
        return "{0}".format(self.name)

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
    slug = models.SlugField(max_length=100, allow_unicode=True, null=True, blank=True)
    name = models.CharField('نام مجری', max_length=100, unique=True)
    surname = models.PositiveSmallIntegerField('عنوان مجری',
                                               choices=PROCTOR_SURNAME,
                                               null=True)
    entry_datetime = models.DateTimeField('تاریخ و زمان ثبت ', null=True)
    pic = models.ImageField(upload_to=picture_path, verbose_name='عکس پرسنلی',
                            help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
                            null=True, blank=True)
    description = models.TextField('توضیحات ضروری مجری', null=True)
    chat = GenericRelation(Chat)

    @property
    def proctor_surname(self):
        proctor_surname = dict(PROCTOR_SURNAME)[self.surname]
        return proctor_surname

    @proctor_surname.setter
    def proctor_surname(self, new_surname):
        revers_surname_dict = {v: k for k, v in dict(PROCTOR_SURNAME).items()}
        self.surname = revers_surname_dict.get(new_surname)

    def get_absolute_url(self):
        params = {'proctor_slug': self.slug}
        return reverse('sa_plan_app:proctor-description', kwargs=params)

    # def get_absolute_url(self):
    #     params = {'proctor_name': self.name}
    #     return reverse('sa_plan_app:proctor-description', kwargs=params)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '-')
        super(Proctor, self).save(*args, **kwargs)

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
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# TODO: این مدل برای توضیحات کارتهای صفحه اصلی (اطلاعات تکمیلی) ایجاد شد ولی بعدا منصرف شدم
# class MoreInfo(models.Model):
#     info_card = models.ForeignKey('InfoCard', on_delete=models.CASCADE, verbose_name='توضیحات مربوط به چیست')
#     name = models.CharField('عنوان کارت', max_length=150, null=True)
#     title = models.CharField('عنوان بازشو کارت', max_length=150, null=True)
#     card_content = models.TextField('مطالب کارت', null=True)
#     card_pic = models.ImageField(upload_to=picture_path,
#                                  verbose_name='عکس کارت',
#                                  help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
#                                  null=True, blank=True)
#     thumbnail_pic = models.ImageField(upload_to=picture_path,
#                                       verbose_name='عکس بند انگشتی',
#                                       help_text='لطفا تصویر مناسبی رااز کامپیوتر تان انتخاب کنید',
#                                       null=True, blank=True)
#     action_link = models.CharField('لینک تصویر', max_length=100, blank=True,
#                                    null=True)
#
#     def __str__(self):
#         return "{0}-->>".format(self.name)
