import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'plan_site.settings')
import django

django.setup()
#   #################
from datetime import datetime
from django.utils import timezone
from faker import Faker
# import random
from sa_plan_app.models import Plans, Proctor, Projects

# from assignments_app.models import MoneyOrder
# from accounts.models import User, UserProfileInfo
# from costcenter.models import CategoryCost, Assistant, Staff, State, Township, PostOffice
#   #################
print('proctor RUN')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('proctor RUN')
#   ######################

fake = Faker('fa_IR')
ff = fake.url()
print(ff)
# print(timezone.now())
date_now = datetime.now()
print('datetime =', date_now)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
zone_time = timezone.now()
print('timezone =', zone_time)
#   #########   PROCTOR FIELDS    #############

proctor_name = ['حسین نعمتی', 'میثم حسینی لر', 'محمد محسنی', 'قادری', 'زرگوش']
proctor_job = ['معاون وزیر رئیس هیات مدیره و مدیر عامل', 'عضو هیات مدیر',
               'معاون فنی و بازرگانی مدیر عامل', 'معاون فن اوری اطلاعات مدیر عامل',
               'معاون پشتیبانی و توسعه مدیریت مدیر عامل']

proctor_job1 = [1, 2, 3, 4, 5]
#   #########   PLAN FIELDS    #############

# plan_name = ['طرح توسعه زیر ساخت', 'طرح کد پستی', 'طرح فن آوری', 'طرح مقاوم سازی', 'طرح خدمات اجباری روستایی']
plan_name = [1, 2, 3, 4, 5]
beneficiary_code = '283100'
plan_typ = [1, 2]
#   #########   PROJECT FIELDS    #############

proj_name = ['پروژه اول', 'پروژه دوم', 'پروژه سوم', 'پروژه چهارم']
prj_no = ['اول', 'دوم', 'سوم', 'چهارم']


def add_plan(n=5):
    for _ in range(n):
        pl_number = str(fake.pyint(min_value=800, max_value=10000, step=5))
        plan_type = fake.random.choice(plan_typ)
        prj_quantity = fake.random.randint(a=1, b=4)
        pl_str_date = fake.date_this_year()
        pl_end_date = fake.future_date()
        credit = fake.pyint(min_value=777, max_value=9999999, step=146)
        pln = Plans.objects.get_or_create(
            name=plan_name[_], organization=1, number=pl_number, beneficiary=1,
            beneficiary_code=beneficiary_code, type=plan_type, project_quantity=prj_quantity, start_date=pl_str_date,
            end_date=pl_end_date, entry_datetime=zone_time, credit=credit)[0]

        #   #######################


def add_project(n):
    for _ in range(n):
        #   #######################
        plan = Plans.objects.all()[fake.random.randint(a=0, b=4)]
        prj_name = 'پروژه ' + str(_) + ' ام از ' + str(plan)
        prj_number = str(fake.pyint(min_value=525, max_value=10000, step=5))
        prj_str_date = fake.date_this_year()
        prj_end_date = fake.future_date()
        credit = fake.pyint(min_value=100, max_value=8000, step=100)
        Projects.objects.get_or_create(
            plan=plan, name=prj_name, number=prj_number, start_date=prj_str_date, end_date=prj_end_date,
            entry_datetime=zone_time, credit=credit)


def add_proctor():
    for _ in range(len(proctor_name)):
        plan = Plans.objects.all()[fake.random.randint(a=0, b=4)]
        proctor = Proctor.objects.get_or_create(
            plan=plan, name=proctor_name[_], surname=proctor_job[_], entry_datetime=zone_time)[0]


if __name__ == '__main__':
    add_plan()
    add_project(15)
    add_proctor()
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('proctor RUN COMPLETE')
