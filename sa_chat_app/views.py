# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}

from django.shortcuts import render

# Create your views here.
# from .models import *
# from sa_plan_app.models import Plan, Project, Proctor, InfoCard, ImageGallery
# from sa_account_app.models import User


def chat(request):
    return render(request, 'sa_chat_app/chat.html')
# def chat(request, uid):
#     ctx = {'chats': Chat.objects.get(user_id=uid)}
#     return render(request, 'sa_chat_app/chat.html', ctx)
