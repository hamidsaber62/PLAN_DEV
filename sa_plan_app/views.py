from django.shortcuts import render

# Create your views here.
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
# from .forms import ProctorForm


def proctor_description(request, pid):
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('pid =', pid)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@')
    if request.user.is_authenticated:
        ctx = {'proctor_des': Proctor.objects.get(id=pid)}
        return render(request, 'sa_plan_app/proctor_description.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponse('برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')

# TODO if don't attachment document in The DB Error Show
#  in plan description page


# @login_required()
def plan_description(request, pid):
    if request.user.is_authenticated:
        ctx = {'plan_des': Plan.objects.get(id=pid)}
        ctx.update({'attachment_file': AttachmentFile.objects.get(object_id=pid)})
        # ctx.update({'prj': Project.objects.get(Plans.name)})
        return render(request, 'sa_plan_app/plan_description.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponse('برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')


# @login_required()
def plan(request):
    if request.user.is_authenticated:
        ctx = {'plan_record': Plan.objects.order_by('entry_datetime')}
        ctx.update({'proctor': Proctor.objects.order_by('plan')})
        return render(request, 'sa_plan_app/plan.html', ctx)
    else:
        messages.warning(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        messages.error(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        messages.success(request, 'برای مشاهده جزئیات باید قبلا ثبت نام و وارد سایت شده باشید')
        return HttpResponseRedirect(reverse('sa_plan_app:index'))


def index(request):
    ctx = {'info_card': InfoCard.objects.all()}
    ctx.update({'carousel': ImageGallery.objects.all()})
    return render(request, 'sa_plan_app/index.html', ctx)


@login_required()
def project(request):
    ctx = {'project_record': Project.objects.all()}
    return render(request, 'sa_plan_app/project.html', ctx)


@login_required()
def proctors(request):
    ctx = {'proctors_record': Proctor.objects.all()}
    return render(request, 'sa_plan_app/proctors.html', ctx)

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

# @login_required()
