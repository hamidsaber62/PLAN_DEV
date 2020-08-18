# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~<START>    With God's help     </START>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}
# {#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#}

from django.shortcuts import render

# Create your views here.
from .models import Chat
from sa_plan_app.models import Plan
# from sa_account_app.models import User


def chat(request, uid):
    cht = Chat.objects.filter(user_id=uid)
    # ctx = {'chats': cht}
    # cht.filter(user_id=uid).only(object)
    # cht1 = Chat.objects.filter(object_id=(cht.filter(user_id=uid)).object_id)
    cht1 = Chat.objects.filter(object_id=cht.get(user_id=uid).object_id)
    ctx = {'chats': cht1}
    # ctx.update(cht1)
    return render(request, 'sa_chat_app/chat.html', ctx)
