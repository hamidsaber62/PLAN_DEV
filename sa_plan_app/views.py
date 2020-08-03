# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}

from django.shortcuts import render
# Create your views here.

from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


# from .forms import ProctorForm

def more_info(request, card_slug):
    ctx = {'info_card': InfoCard.objects.get(slug=card_slug)}
    print(ctx)
    return render(request, 'sa_plan_app/more-info.html', ctx)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def proctor_description(request, proctor_slug):
    if request.user.is_authenticated:
        ctx = {'proctor': Proctor.objects.get(slug=proctor_slug)}
        return render(request, 'sa_plan_app/proctor-description.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponse('برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')


# TODO if don't attachment document in The DB Error Show
#  in plan description page


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @login_required()
def plan_description(request, plan_slug, plan_id):
    if request.user.is_authenticated:
        """
         برای نمایش نام طرح در آدرس بار دو روش را پیاده کردم اول با سه خط پایین که کامنت شده اند 
         و دوم دو خط بعد از این سند تابع در هر دو حالت به اجبار باید نام طرح و کد آن را پاس بدهیم 
         چون هدف نمایش نمایش نام طرح در آدرس بار است و در این سه خط از هر دو استفاده کردم و در دومین راه 
          فقط از کد استفاده کردم ولی برای نمایش نام مجبور به پاس دادن هر دو هستیم به هر حال در 
         هر دو روش آدرس بار نام و کد طرح را نمایش میدهد و خواسته ما نیز همین بوده است برای زیبایی بیشتر و سئوی گوگل 
        
        # revers_key_plan_name = {v: k for k, v in dict(PLAN_NAME).items()}
        # num_plan_name = revers_key_plan_name.get(plan_name)
        # ctx = pln = {'plan_des': Plan.objects.get(key_plan_name=num_plan_name)}
"""
        # ctx = {'plan_des': Plan.objects.get(key_plan_name=pln1.key_plan_name)}
        pln1 = Plan.objects.get(id=plan_id)
        # print(pln1, type(pln1), pln1.id, pln1.name, pln1.key_plan_name)
        ctx = {'plan_des': Plan.objects.get(id=plan_id)}

        att = {'attachment': AttachmentFile.objects.filter(object_id=plan_id)}
        ctx.update(att)
        poj = {'project': Project.objects.filter(plan=Plan.objects.get(id=plan_id))}
        ctx.update(poj)
        return render(request, 'sa_plan_app/plan-description.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponse('برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @login_required()
def plan(request):
    if request.user.is_authenticated:
        ctx = {'plan': Plan.objects.order_by('entry_datetime')}
        ctx.update({'proctor': Proctor.objects.order_by('plan')})
        return render(request, 'sa_plan_app/plan.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        messages.error(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        messages.success(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponseRedirect(reverse('sa_plan_app:index'))


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def index(request):
    ctx = {'info_card': InfoCard.objects.all()}
    ctx.update({'gallery': ImageGallery.objects.all()})
    return render(request, 'sa_plan_app/index.html', ctx)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@login_required()
def project(request, project_slug):
    ctx = {'project': Project.objects.get(slug=project_slug)}
    return render(request, 'sa_plan_app/project.html', ctx)


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def proctor(request):
#     if request.method == 'POST':
#         filled_form = ProctorForm(request.POST)
#         if filled_form.is_valid():
#             note = 'ثبت نام آقای %s ، به عنوان مجری انجام شد' % (filled_form.cleaned_data['name'])
#                                                                     #   , filled_form.cleaned_data[''])
#
#             new_form = ProctorForm()
#             return render(request, 'sa_plan_app/proctors.html', {'proctorform': new_form, 'note': note})
#     else:
#         form = ProctorForm()
#         return render(request, 'sa_plan_app/proctors.html', {'proctorform': form})

# def admin(request):
#     return HttpResponse(request, 'admin/')


# def project_description(request, pid):
#     ctx = {'project_des': ProjectDescription.objects.get(id=pid)}
#     return render(request, 'sa_plan_app/project_description.html', ctx)
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
